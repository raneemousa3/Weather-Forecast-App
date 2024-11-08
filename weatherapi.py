import requests
import matplotlib.pyplot as plt
import streamlit as st
import time
#technologies used: python oop, matplotlib, streamlit,pandas
class Weather:
    def __init__(self,days,postalcode,country,city,state=""):
        self.apiurl=None
        self.city=city
        self.times={}
        self.temperatures={} #initialising attributes for the weather
        self.days=days
        self.hour_temp=None
        self.hourly_temp=None
        self.country=country
        self.longitude=None
        self.latitude=None  
        self.response=None
        self.state=state
        self.postalcode=postalcode
        self.current_temp=0#getting back data as json
        self.get_Long_Lat()
        self.get_response()
        self.get_temp()
        
    def get_response(self):
      # Send request to the API and parse the response in json
     self.apiurl = f"https://api.open-meteo.com/v1/dwd-icon?latitude={self.latitude}&longitude={self.longitude}&current=temperature_2m&hourly=temperature_2m&forecast_days={self.days}"
    
     self.response = requests.get(self.apiurl).json()
     for i in self.response:
         print(i)
         print()
      # Return the JSON response
    def get_Long_Lat(self):
        url = f"https://api.geoapify.com/v1/geocode/autocomplete?text={self.city}&apiKey=8b3e8ad1c1a043ce8fff2da8c3c816f8"
        response=requests.get(url).json() 

        if self.country!="United States of America":
            for i in response['features']:
             if i['properties']['country']==self.country :

        
                self.latitude=i['properties']['lat']
                self.longitude=i['properties']['lon']
                break
        else :
           for i in response['features']:
             if i['properties']['state']==self.state :
                self.latitude=i['properties']['lat']
                self.longitude=i['properties']['lon']
                break

    def get_temp(self):
        self.hour_temp=self.response['hourly']
        print(self.hour_temp)
        self.hourly_temp=self.hour_temp['temperature_2m']
        for temperature, timestamp in zip(self.hourly_temp, self.hour_temp['time'] ):
            oflist=timestamp.split('T')
            if oflist[0] not in self.temperatures:
                self.temperatures[oflist[0]]=[temperature]
            else:
                self.temperatures[oflist[0]].append(temperature)
            
        print(self.temperatures) #getting temperatures of each day as dict
    def current_Temp(self):
        self.current_temp=self.response['current']['temperature_2m']
        return self.current_temp
        #'current': {'time': '2024-11-08T01:45', 'interval': 900, 'temperature_2m': 10.4}
        


    def get_time(self):
        Timeofday=self.hour_temp['time']
        print(Timeofday)
        for datetime in Timeofday:      #getting  time as dicts with the date as the key
            oflist=datetime.split('T')
            if oflist[0] not in self.times:
                self.times[oflist[0]]=[oflist[1]]
            else:
                self.times[oflist[0]].append(oflist[1])
        
        #print(self.times)
    def graph_it(self):
       for key in self.times:
         plt.plot(self.times[key],self.temperatures[key],label=str(key))
         plt.xlabel('Time of Day')
         plt.ylabel('Temperature (°C)')
         plt.title('Hourly Temperature in '+self.city+", "+ self.country)
         plt.xticks(rotation=45)  #graphing time vs temperature for each day 
         plt.legend()
       st.pyplot(plt)
    def display_weather_analysis(self):
    # Analyze the current temperature and display appropriate message and icon
   
        col1, col2 = st.columns([1, 3]) 

        if self.current_temp > 30:
            icon_url = "https://cdn0.iconfinder.com/data/icons/season-outline-filled/614/12_-_Sunny-1024.png"
            description = f"The current temperature is {self.current_temp}°C. It's very hot! Stay hydrated and avoid the sun if possible."
        elif self.current_temp > 20:
            icon_url = "https://cdn0.iconfinder.com/data/icons/season-outline-filled/614/12_-_Sunny-1024.png"
            description = f"The current temperature is {self.current_temp}°C. It's sunny, enjoy the warmth!"
        elif self.current_temp >= 10:
            icon_url = "https://th.bing.com/th/id/OIP.8fHU00Aw-fjeRlSkfPwPuQAAAA?rs=1&pid=ImgDetMain"
            description = f"The current temperature is {self.current_temp}°C. It's a mild day, perfect for a light jacket!"
        elif self.current_temp >= 0:
            icon_url = "https://as2.ftcdn.net/v2/jpg/02/73/87/43/1000_F_273874329_SN3lxBR0UL3R9FMiRBKu5O0aXx97Y3Fr.jpg"
            description = f"The current temperature is {self.current_temp}°C. It's quite cold, be sure to wear something warm!"
        else:
            icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Snowflake_icon.svg/120px-Snowflake_icon.svg.png"
            description = f"The current temperature is {self.current_temp}°C. It's freezing cold! Stay warm and bundle up!"

        # Show the icon and description in the columns
        with col1:
           st.markdown(
                f"""
                <div style="border-radius: 50%; overflow: hidden; width: 100px; height: 100px;margin: 10px">
                    <img src="{icon_url}" width="100" height="100" />
                </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h4 style='color: white; text-align: left;'>{description}</h4>", unsafe_allow_html=True)


def create_webpage():
    st.set_page_config(page_title='top songs analysis', page_icon=':muciscal_note:')
    #st.title("<h5 style='text-align: center;font-family: sans-serif;font-size: small;'>Analysis for your top songs</h5>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Weather forcast</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Learn More about the weather in your Area</h5>", unsafe_allow_html=True)
  
    NumOfDays = st.slider("Select the Number of days you want to see the weather for", 1, 7)
    Countryname = st.selectbox(' Select the Country you live in', 


['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 

    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 

    'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 

    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 

    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Congo-Brazzaville)', 'Congo (Democratic Republic)', 

    'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czechia (Czech Republic)', 'Denmark', 'Djibouti', 

    'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 

    'Eswatini (Swaziland)', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 

    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 

    'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Jordan', 

    'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'South Korea', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 

    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 

    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 

    'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 

    'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 

    'Pakistan', 'Palau', 'Palestine State', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 

    'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 

    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 

    'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 

    'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 

    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 

    'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 

    'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 

    'Zimbabwe'

], )
    if Countryname=="United States of America":
         state = st.selectbox(' Select the State you live in', [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", 
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
    "Wisconsin", "Wyoming"

],)
    else:
        state=None
         
    city= st.text_input("Enter your city:")
    PostalCode= st.text_input("Enter your zipcode:")
    return NumOfDays,PostalCode,Countryname,city,state

def main():
    """
    Call functions for streamlit exectution
    """
    try:
    

        NumOfDays,PostalCode,Countryname,city,state=create_webpage()
        st.balloons ()
        with st.spinner( 'Weather Chart in Process'):
            time.sleep(12)
        
        weather=Weather(NumOfDays,PostalCode,Countryname,city,state)

        st.write("Current Weather:", weather.current_Temp(), " C")
        weather.display_weather_analysis()
        #weather=Weather(4,"02215","United States of America","Boston","Massachusetts")
        weather.get_time()
        weather.graph_it()
    except  Exception as e:
        st.error("Weather for Location not found")
  
    
 
main()
