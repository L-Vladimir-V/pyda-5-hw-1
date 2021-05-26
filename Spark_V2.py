----all-----
df = spark.read.option('header', True).format('csv').load('owid-covid-data.csv')
df.createOrReplaceTempView('covid') 
----1-----
>>> sqlDF = spark.sql("SELECT iso_code, location, round(total_cases*100/population,2) as pr 
					   FROM covid 
					   WHERE date = '2021-03-31' and iso_code not like 'OWID%' 
					   ORDER BY cast(pr as int) desc nulls last")

----2-----
>>> sqlDF = spark.sql("SELECT date, location, new_cases 
                      FROM covid 
                      WHERE cast(date as date) between '2021-03-25' and  '2021-03-31'  and iso_code not like 'OWID%' 
                      ORDER BY cast(new_cases as int) desc")
----3-----
>>> sqlDF = spark.sql("SELECT  date, LAG(new_cases) OVER(ORDER BY date) prev_cases, new_cases, (new_cases - LAG(new_cases) OVER(ORDER BY date)) as delta  
                       FROM covid 
                       WHERE cast(date as date) between '2021-03-24' and  '2021-03-31'  and location = 'Russia'")
                       
df.select('iso_code','location','population','icu_patients','date').where(df.location.startswith('Ru')).show(10)