----all-----
df = spark.read.option('header', True).format('csv').load('owid-covid-data.csv')
df.createOrReplaceTempView('covid') 
----1-----
>>> sqlDF = spark.sql("SELECT iso_code, location, population, total_cases  
					   FROM covid 
					   WHERE date = '2021-03-31' and iso_code not like 'OWID%' 
					   ORDER BY cast(total_cases as int) desc nulls last")

----2-----
>>> sqlDF = spark.sql("SELECT location, sum_case 
                       FROM( SELECT  location, sum(new_cases) as sum_case 
                             FROM covid 
                             WHERE cast(date as date) between '2021-03-25' and  '2021-03-31'  and iso_code not like 'OWID%' 
                             GROUP BY location)
                       ORDER BY sum_case DESC nulls last")
----3-----
>>> sqlDF = spark.sql("SELECT  date, LAG(new_cases) OVER(ORDER BY date) prev_cases, new_cases, (new_cases - LAG(new_cases) OVER(ORDER BY date)) as delta  
                       FROM covid 
                       WHERE cast(date as date) between '2021-03-24' and  '2021-03-31'  and location = 'Russia' 
                       LIMIT 3")
df.select('iso_code','location','population','icu_patients','date').where(df.location.startswith('Ru')).show(10)