import streamlit as st

st.markdown("# Umesh Narayanappa")
st.markdown("### Senior Data Analyst")
st.markdown("""
    I am a Data Science and Analytics Enthusiast, passionate about adding value to the business through data insights. 
    I have experience of working through entire life cycle of data science project starting with data collection, 
    data cleaning, data analysis, data visualization and model building.
""")


st.markdown("### Certifications")
st.markdown("""
    Below mentioned certifications helps me to keep myself updated with the skills required :
""")
st.markdown("""
    * Udacity - Data Analyst Nano Degree Certified
    * Alteryx - Designer Core Certified    
    * DataCamp - Data Analyst Certified
    * AWS - Machine Learning Specialist
""")



st.markdown("### R Shiny Apps - Cloud Hosted")
st.markdown("""
    Shiny is an R package that makes it easy to build interactive web apps straight from R. 
    You can host standalone apps on a webpage or embed them in R Markdown documents or build dashboards. 
    Below are some of the apps which I have developed completely using R Shiny and different R packages.
""")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/Covid19USAStatesandCounties.PNG")

    with text_col:
        st.markdown("[Covid-19 Tracker by States in USA](https://covid19tracking.shinyapps.io/Covid19USAStatesandCounties/)")
        st.write("""Application lets you to interactively explore the Coronavirus cases and deaths in every county of the selected state.
            """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/Covid19_USA_Numbers.PNG")

    with text_col:
        st.markdown("[Covid-19 Tracker by States in USA](https://covid19tracking.shinyapps.io/Covid19USAStatesandCounties/)")
        st.write("""This application lets you to view the Covid Cases and Deaths at country level through visuals.
            """)


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/ChicagoCrime2016.PNG")

    with text_col:
        st.markdown("[Crimes in Chicago 2016](https://umeshjn.shinyapps.io/ChicagoCrimes2016/)")
        st.write("""
        Crimes in Chicago was one of the hottest topics during the 2016 Presidential Elections. 
        Here is a dashboard built using the open dataset provided by the government agencies.
        """)


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/OnlineTutoring.PNG")

    with text_col:
        st.markdown("[Online Tutoring Sales Lead Monthly Dashboard](https://umeshjn.shinyapps.io/RDashboard/)")
        st.write("""
        Online tutoring is a amazing business in today's world generating billions of revenues. 
        This dashboard uses a dummy data for online sales of tutoring based on the leads.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/AustralianPopulation.PNG")

    with text_col:
        st.markdown("[Australian Population](https://umeshjn.shinyapps.io/AustralianPopulation-2016/)")
        st.write("""
        Australia is the largest country in Oceania and the world's sixth-largest country by total area.
        This application lets you explore the population of the continent among different age groups. 
        This data is from Australian Bureau of Satistics.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/USConsumerFinancialComplaints.PNG")

    with text_col:
        st.markdown("[US Consumer Financial Complaints](https://umeshjn.shinyapps.io/usconsumerfinancialcomplaints/)")
        st.write("""
        Consumer complaints across different financial products is recorded and tracked by 
        the government agencies for making sure the financial firms provide the right service to the customers. 
        This dashboard gives you sneak peak into those complaints.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/IndianStocks.PNG")

    with text_col:
        st.markdown("[Coffee Can Investing - Indian Stocks](https://umeshjn.shinyapps.io/CoffeeCanInvesting/)")
        st.write("""
        Compound interest is the eight wonder of the world. Investing in equities is one of the best options for common people 
        to help them grow their wealth. This application helps someone who wants to know how their wealth would have grown
        by investing in Indian stocks.
        """)


st.markdown("### Python Based Data Apps")
st.markdown("""
    Streamlit is one of the best frameworks available for development of the python data applications. 
    Below is some of the apps which are developed using Python Streamlit package.
""")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/CoffeeCan.PNG")

    with text_col:
        st.markdown("[Coffee Can Investing](https://share.streamlit.io/umeshjn/streamlit-coffeecaninvesting/main/app.py)")
        st.write("""
         … the coffee can portfolio is designed to protect you against yourself—the obsession with checking stock prices
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/dailycovid.PNG")

    with text_col:
        st.markdown("[Daily Covid Numbers in USA](https://share.streamlit.io/umeshjn/streamlit-usa-dailycovid19/main/app.py)")
        st.write("""
         Covid-19 - the virus which brough the all powerful humans to their knees since last two years, it has wrecked havoc like never seen before and devasted the individuals, families, states, countries and the world as a whole.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/compounding.PNG")

    with text_col:
        st.markdown("[Power of Compounding](https://share.streamlit.io/umeshjn/streamlit-powerofcompounding/main/app.py)")
        st.write("""
        Albert Einstein once said that Compound interest is the eighth wonder of the world. He who understands it, earns it ... he who doesn't ... pays it..
        """)    

st.markdown("### Data Visualizations (Tableau & R)")
st.markdown("""
    Tableau helps is presenting the data to the end customers through data visualizations and dashboards.
    Working using tableau is amazing experience and the ability it brings to the table for data presentation through visualizations is very nice.
    Tableau has changed the field of Data Visualization Dashboarding since last many years.
""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/nyscancerviz.PNG")

    with text_col:
        st.markdown("[New York State Cancer Death Rates 1976-2018]()")
        st.write("""
        Humanity has been fighting a brave war with the cancer and the progress made since last 4-5 decades shows that there is lot of optimism. 
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/drugoverdosedeathrates.PNG")

    with text_col:
        st.markdown("[Drug Overdose Deaths in USA 2014-2019]()")
        st.write("""
        Drug Overdose is one of the most biggest health concerns in America and this visualization gives you the view of Drug Overdose Death Rates 2014-2019. 
        """)
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/seattlecrimes.PNG")

    with text_col:
        st.markdown("[Seattle Crimes Numbers Reported between 2008 and 2017]()")
        st.write("""
        Crimes in the cities are the biggest challenges for the law and order authorities. This dashboard view gives a glimpse of Seattle crimes numbers between 2008 and 2017. 
        """)
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/spiders_northamerica.PNG")

    with text_col:
        st.markdown("[Spider Species Identified in North America]()")
        st.write("""
        There are over 45000 spider spieces in the world and 7000 out of those are in North American Countries. 
        """)
        
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/cdc_overdoserates.PNG")

    with text_col:
        st.markdown("[Overdose Death Rates Involving Opiods between 1999-2019]()")
        st.write("""
        Overdose death rates due to Synthetic Opioids has gone up by 38 times between 1999 and 2019. 
        """)
        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/GunViolence.png")

    with text_col:
        st.markdown("[Gun Violence in America](https://public.tableau.com/app/profile/umeshjn/viz/GunViolenceinAmerica_0/GunViolence)")
        st.write("""
        This dashboard gives you a view of the gun violence reported across America from 2014 to 2017.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/911-MontgomeryCounty.png")

    with text_col:
        st.markdown("[Montgomery County - 911 Calls](https://public.tableau.com/app/profile/umeshjn/viz/911-MontgomeryCounty/911-MontgomeryCounty)")
        st.write("""
        This dashboard gives you a view of 911 Emergency Calls made in Montgomery County, PA.
        """)


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/ChicagoBiCycleSharing.png")

    with text_col:
        st.markdown("[Bicycle Sharing in Chicago](https://public.tableau.com/app/profile/umeshjn/viz/ChicagoBicycleSharing/ChicagoBiCycleSharing)")
        st.write("""
        This dashboard gives you a view of bicycle hiring in Chicago from 2014 to 2017.
        """)



with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/NobelPrizes.png")

    with text_col:
        st.markdown("[Nobel Laureates 1901-2016](https://public.tableau.com/app/profile/umeshjn/viz/Nobel_15/NobelPrizes)")
        st.write("""
        This dashboard gives you a view of the Nobel Prizes from 1901 to 2016.
        """)

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/NyCityAirbnbLIsting.png")

    with text_col:
        st.markdown("[Airbnb Listings in NewYork City](https://public.tableau.com/app/profile/umeshjn/viz/AirbnbNewYorkCityListings_16316414938610/NyCityAirbnbLIsting)")
        st.write("""
        Interactive Dashboard to View the Map of the Airbnb listings in NewYork City
        """)


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/AfricanPopulation.png")

    with text_col:
        st.markdown("[African Population](https://public.tableau.com/app/profile/umeshjn/viz/AfricanPopulation2021/Dashboard1)")
        st.write("""
        View of the African Population in 2021.
        """)


st.markdown("### Data Stories Blog")
st.markdown("[Dataasana](https://www.dataasana.com/)")
st.markdown("""
    Ability to explore the data and tell the story hidden inside a table of data is very important skill for any data analyst.
    This blog which I have created helps me to learn that skill. Here I have written data stories based on some of the topics which
    are interesting to me. This is kind of learning for me.
""")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/stockbeginners.PNG")

    with text_col:
        st.markdown("[Beginner Guide to Indian Stock Market Investing](https://www.dataasana.com/posts/2020-05-21-beginner-guide-to-indian-stock-market-investing/)")
        st.write("""
        Stock Market is the only way for growing ones wealth for vast majority of the people. Majority of them fail to use this wonderful investing option.
        """)


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/covidblog.PNG")

    with text_col:
        st.markdown("[Covid-19 and the USA](https://www.dataasana.com/posts/2020-05-11-covid-19-and-usa/)")
        st.write("""
        Covid-19 the virus which originated in China and spread across the world. The health crisis leading to economic crisis. Killing the most vulnerable population and impacting the lives of millions.
        """)

        
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("images/deathrates2.PNG")

    with text_col:
        st.markdown("[Cancer in NewYork State 1976-2018](https://www.dataasana.com/posts/2020-09-24-newyorkstate-cancer/)")
        st.write("""
        Humanity has been fighting the war with cancer for long time and the numbers of New York State shows that there is great progress. All thanks to the advancements in the field of science and technology which has made this possible.
        """)
        
        
