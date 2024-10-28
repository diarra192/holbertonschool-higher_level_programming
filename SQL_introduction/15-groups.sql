-- This command selects the scores and the number of records for each score from the `second_table`, ordered by the number of records in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
