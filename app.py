import streamlit as st

st.markdown("# Umesh Narayanappa")
st.markdown("### Senior Data Engineer")
st.markdown("""
    **I'm a passionate Data Engineering and Analytics professional with hands-on experience across the full lifecycle of data science projects. From data collection and cleaning to analysis, visualization, and even model building, I work to turn raw data into actionable insights. Proficient in leveraging the latest tools and technologies, I help businesses understand and harness their data by building efficient data pipelines that gather, clean, and structure information from diverse sources. I also design intuitive dashboards to present findings to both technical and non-technical stakeholders, enabling data-driven decision-making at all levels.**
""")


st.markdown("***This web app is created to give you a glimpse into my skills and all these are built out of my own personal interest in the data and the topics***")

st.markdown("### Data Apps built using Python")
st.markdown("""
    Streamlit is one of the best frameworks available for development of the python data applications. 
    Below is some of the apps which are developed using Python Streamlit package.
""")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Coffee Can Investing](https://share.streamlit.io/umeshjn/streamlit-coffeecaninvesting/main/app.py)")
        st.write("""
         … the coffee can portfolio is designed to protect you against yourself—the obsession with checking stock prices
        """)
        st.image("images/CoffeeCan.PNG")

    with col2:
        st.markdown("[Daily Covid Numbers in USA](https://share.streamlit.io/umeshjn/streamlit-usa-dailycovid19/main/app.py)")
        st.write("""
         Covid-19 - the virus which brough the all powerful humans to their knees since last two years, it has wrecked havoc like never seen before and devasted the individuals, families, states, countries and the world as a whole.
        """)
        st.image("images/dailycovid.PNG")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Power of Compounding](https://share.streamlit.io/umeshjn/streamlit-powerofcompounding/main/app.py)")
        st.write("""
        Albert Einstein once said that Compound interest is the eighth wonder of the world. He who understands it, earns it ... he who doesn't ... pays it..
        """)   
        st.image("images/compounding.PNG")

    with col2:
        st.markdown("[Indian Stocks Quarterly Results](https://share.streamlit.io/umeshjn/-streamlit-indians-stocks-quarterly-results/main)")
        st.write("""
         India is one of the fastest growing economies and for the next decade or so should be the top growing economy in the world. Its a great investing opportunity for everyone to make the most out of it specially for the Indian public who have missed out greatly the last 30-40 years of Indian growth story. This application lets you see the results of some of the well known companies in the country.
        """)
        st.image("images/quarterly.PNG")


st.markdown("### Python and Data (Jupyter Notebooks)")
st.markdown("""
    Jupyter Notebooks is a great tool for all the data science tasks from exploring, visualizing, model building to presenting the data stories to the target audience.
""")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Exploring Baltimore City Salaries Dataset](https://github.com/umeshjn/jupyternotebooks/blob/f5663a4b0dfb98f19f1ccf3920f76651d4516313/Exploring%20Baltimore%20City%20Employee%20Salaries%20Data.ipynb)")
        st.write("""
            City administration is like running a huge company. Like any corporate, it requires lot of people and each of them will be paid salaries. This notebook explores the salaries dataset for the city of Baltimore.
        """)
        st.image("images/baltimoresalaries.PNG")

    with col2:
        st.markdown("[Exploring Baltimore City 911 Calls Dataset](https://github.com/umeshjn/jupyternotebooks/blob/f5663a4b0dfb98f19f1ccf3920f76651d4516313/Exploring%20Baltimore%20911%20Calls%20Data.ipynb)")
        st.write("""
         911 is a National Emergency services. This notebook explores the 911 calls dataset for the city of Baltimore. Will try to answer few queries based on the data available at hand - Is the community using the service for the intented use? How is the distribution of the calls across the various parameters?
        """)
        st.image("images/baltimore911calls.PNG")


st.markdown("### R Shiny Applications")
st.markdown("***Apps with maps has issue because the highcharter package used for creating the visualizations is giving trouble for maps***")
st.markdown("""
    Shiny is an R package that makes it easy to build interactive web apps straight from R. 
    You can host standalone apps on a webpage or embed them in R Markdown documents or build dashboards. 
    Below are some of the apps which I have developed completely using R Shiny and different R packages.
""")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Covid-19 Tracker by States in USA](https://covid19tracking.shinyapps.io/Covid19USAStatesandCounties/)")
        st.write("""Application lets you to interactively explore the Coronavirus cases and deaths in every county of the selected state.
            """)
        st.image("images/Covid19USAStatesandCounties.PNG")

    with col2:
        st.markdown("[Crimes in Chicago 2016](https://umeshjn.shinyapps.io/ChicagoCrimes2016/)")
        st.write("""
        Crimes in Chicago was one of the hottest topics during the 2016 Presidential Elections. 
        Here is a dashboard built using the open dataset
        """)
        st.image("images/ChicagoCrime2016.PNG")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Online Tutoring Sales Lead Monthly Dashboard](https://umeshjn.shinyapps.io/RDashboard/)")
        st.write("""
        Online tutoring is a amazing business in today's world generating billions of revenues. 
        This dashboard uses a dummy data for online sales of tutoring based on the leads.
        """)
        st.image("images/OnlineTutoring.PNG")

    with col2:
        st.markdown("[Australian Population](https://umeshjn.shinyapps.io/AustralianPopulation-2016/)")
        st.write("""
        Australia is the largest country in Oceania and the world's sixth-largest country by total area.
        This application lets you explore the population of the continent among different age groups. 
        """)
        st.image("images/AustralianPopulation.PNG")
        


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[US Consumer Financial Complaints](https://umeshjn.shinyapps.io/usconsumerfinancialcomplaints/)")
        st.write("""
        Consumer complaints across different financial products is recorded and tracked by 
        the government agencies for making sure the financial firms provide the right service to the customers. 
        This dashboard gives you sneak peak into those complaints.
        """)
        st.image("images/USConsumerFinancialComplaints.PNG")

    with col2:
        st.markdown("[Coffee Can Investing - Indian Stocks](https://umeshjn.shinyapps.io/CoffeeCanInvesting/)")
        st.write("""
        Compound interest is the eight wonder of the world. Investing in equities is one of the best options for common people 
        to help them grow their wealth. This application helps someone who wants to know how their wealth would have grown
        by investing in Indian stocks.
        """)
        st.image("images/IndianStocks.PNG")

st.markdown("### Data Visualizations (Tableau & R)")
st.markdown("""
    Data Visualization is a very powerful tool for presenting the data in a more insightful way to the target audience. 
    Here in this section I present some of the visualizations or dashboards created using real world data sets using technologies like **R and Tableau**.
""")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Covid-19 USA Cases 2020 to 2021](https://public.tableau.com/app/profile/umeshjn/viz/Covid-19CasesUSA/Covid19CaseUSA)")
        st.write("""
        Fight against Covid19 is into third year almost and the numbers are increasing against due to the new variant.
        """)
        st.image("images/Covid19 Case USA.png")

    with col2:
        st.markdown("[Covid Deaths in USA(2020 and 2021)](https://public.tableau.com/app/profile/umeshjn/viz/CovidDeathsinUSA2020and2021/CovidDeathsUSA2020and2021)")
        st.write("""
        So many deaths due to Covid and we have ended up treating them as just statictics which is very sad and painful if you really think about all the people who have lost their loved ones.
        """)
        st.image("images/coviddeaths.png")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("**New York State Cancer Death Rates 1976-2018**")
        st.write("""
        Humanity has been fighting a brave war with the cancer and the progress made since last 4-5 decades shows that there is lot of optimism. 
        """)
        st.image("images/nyscancerviz.PNG")

    with col2:
        st.markdown("**Drug Overdose Deaths in USA 2014-2019**")
        st.write("""
        Drug Overdose is one of the most biggest health concerns in America and this visualization gives you the view of Drug Overdose Death Rates 2014-2019. 
        """)
        st.image("images/drugoverdosedeathrates.PNG")

       

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("**Seattle Crimes Numbers Reported **")
        st.write("""
        Crimes in the cities are the biggest challenges for the law and order authorities. This dashboard view gives a glimpse of Seattle crimes numbers between 2008 and 2017. 
        """)
        st.image("images/seattlecrimes.PNG")

    with col2:
        st.markdown("**Spider Species Identified in North America**")
        st.write("""
        There are over 45000 spider species in the world and 7000 out of those are in North American Countries. 
        """)
        st.image("images/spiders_northamerica.PNG")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Gun Violence in America](https://public.tableau.com/app/profile/umeshjn/viz/GunViolenceinAmerica_0/GunViolence)")
        st.write("""
        This dashboard gives you a view of the gun violence reported across America from 2014 to 2017.
        """)
        st.image("images/GunViolence.png")

    with col2:
        st.markdown("[Montgomery County - 911 Calls](https://public.tableau.com/app/profile/umeshjn/viz/911-MontgomeryCounty/911-MontgomeryCounty)")
        st.write("""
        This dashboard gives you a view of 911 Emergency Calls made in Montgomery County, PA.
        """)
        st.image("images/911-MontgomeryCounty.png")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Bicycle Sharing in Chicago](https://public.tableau.com/app/profile/umeshjn/viz/ChicagoBicycleSharing/ChicagoBiCycleSharing)")
        st.write("""
        This dashboard gives you a view of bicycle hiring in Chicago from 2014 to 2017.
        """)
        st.image("images/ChicagoBiCycleSharing.png")

    with col2:
        st.markdown("[Airbnb Listings in NewYork City](https://public.tableau.com/app/profile/umeshjn/viz/AirbnbNewYorkCityListings_16316414938610/NyCityAirbnbLIsting)")
        st.write("""
        Interactive Dashboard to View the Map of the Airbnb listings in NewYork City
        """)
        st.image("images/NyCityAirbnbLIsting.png")

st.markdown("### Data Stories Blog - RMarkdown")
st.markdown("[Dataasana](https://www.dataasana.com/)")
st.markdown("""
    Ability to explore the data and tell the story hidden inside a table of data is very important skill for any data analyst.
    This blog which I have created helps me to learn that skill. Here I have written data stories based on some of the topics which
    are interesting to me. 
""")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Seattle Crimes 2011-2017](https://www.dataasana.com/posts/2021-01-12-seattle-crimes/)")
        st.write("""
        Crimes is cities is one of the biggest problems for any law enforcements agencies.
        """)
        st.image("images/seattlecrimesstory.PNG")

    with col2:
        st.markdown("[Beginner Guide to Indian Stock Market Investing](https://www.dataasana.com/posts/2020-05-21-beginner-guide-to-indian-stock-market-investing/)")
        st.write("""
        Stock Market is the only way for growing ones wealth for vast majority of the people. Majority of them fail to use this wonderful investing option.
        """)
        st.image("images/stockbeginners.PNG")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Covid-19 and the USA](https://www.dataasana.com/posts/2020-05-11-covid-19-and-usa/)")
        st.write("""
        Covid-19 the virus which originated in China and spread across the world. The health crisis leading to economic crisis. Killing the most vulnerable population and impacting the lives of millions.
        """)
        st.image("images/covidblog.PNG")

    with col2:
        st.markdown("[Cancer in NewYork State 1976-2018](https://www.dataasana.com/posts/2020-09-24-newyorkstate-cancer/)")
        st.write("""
        Humanity has been fighting the war with cancer for long time and the numbers of New York State shows that there is great progress. All thanks to the advancements in the field of science and technology which has made this possible.
        """)
        st.image("images/deathrates2.PNG")
