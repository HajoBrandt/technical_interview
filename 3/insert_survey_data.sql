BULK INSERT survey_results
FROM 'path\survey_results_tabs_seperated.tsv'
WITH (
   FIELDTERMINATOR = '\t',
   ROWTERMINATOR = '\n',
   FIRSTROW = 2,
   TABLOCK
);