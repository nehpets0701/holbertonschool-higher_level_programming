-- lists records with score
SELECT score, count(score) AS number FROM second_table GROUP BY score DESC;
