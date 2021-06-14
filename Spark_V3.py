----all-----
df = spark.read.option('header', True).format('csv').load('owid-covid-data.csv')
df.createOrReplaceTempView('covid') 

----2-----
>>> sqlDF = spark.sql("SELECT date, location, new_cases 
                       FROM 
                            (SELECT date, location, new_cases, rank()over(partition by location order by cast(new_cases as int) desc) rk 
                            FROM covid 
                            WHERE cast(date as date) between '2021-03-25' and  '2021-03-31'  and iso_code not like 'OWID%' ORDER BY cast(new_cases as int) desc)
                       WHERE rk = 1")
 >>>sqlDF.show(10)                      
