# NMC

A few days ago I saw a post on twitter that did a basic analysis on data about doctors in Nepal. It listed some basic information such as the breakdown of gender, last names, home district, etc. indivudualy. Somebody had asked for the source of their information at that time.  After thinking about their analysis I thougth I could play around and get the data myself from the [Nepal Medical Council](www.nmc.org.np) website.  

So,  I decided to write a simple python script that would serially pull off the available information on those doctors. and write it on the sqlite file.

Data on all the registered doctors from NMC_No 1 to 20387 was extracted from nmc.org.np site and added to `nmc.db` file. The five columns are as follows:  
    - Full Name
    - NMC number
    - Full Address
    - Gender
    - Degree

Unfortunately, this particular website doesn't track where they currently live, or work, or if they even practice actively. We will assume thta this information is correct and use it as if this is correct informaation.

The data available in `data/nmc.db` is not the same as reported on the nmc.org.np website. The website lists that there are 26K + bachelor level doctors, and 7k+ masters level.
