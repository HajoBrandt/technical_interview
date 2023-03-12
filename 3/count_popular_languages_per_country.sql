use localhost	
SELECT Country,
       COUNT(CASE WHEN LanguageHaveWorkedWith LIKE '%C++%' THEN 1 END) AS 'C++',
       COUNT(CASE WHEN LanguageHaveWorkedWith LIKE '%Python%' THEN 1 END) AS 'Python',
       COUNT(CASE WHEN LanguageHaveWorkedWith LIKE '%HTML/CSS%' THEN 1 END) AS 'HTML/CSS'
FROM dbo.survey_results	
GROUP BY Country