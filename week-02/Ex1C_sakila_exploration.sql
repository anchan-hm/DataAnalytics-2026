/*
a) The information that is in this table are actor_id, first_name, last_name, and last_update. 
b) The information that is in this table are film_id, title, description, release_year, language_id, original_language_id,
rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update. 
c) The table that contains both actor_id and film_id is film_actor
d) This table contains the rental_id, rental_date, inventory_id, customer_id, return_date, staff_id,
and last_update. This table is easy to read because it has simple entries. 
e) This table contains inventory_id, film_id, store_id and last_update. 
f) The table I would use for the films rented on specific dates would be the rental table. They're related, because the inventory are the films themselves and
it can be used to understand how long the films were rented for in rental. 
*/ 

SELECT * FROM rental;
SELECT * FROM inventory; 
SELECT * FROM film;