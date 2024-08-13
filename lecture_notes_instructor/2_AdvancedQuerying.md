## Learning Objectives

- The students should be able to apply advanced querying techniques using SQLAlchemy, such as filtering data and performing joins with custom query builders.
- The students should be able to demonstrate an understanding of ORM optimization techniques like pagination for large data sets.
- The students should be able to explain the concepts of lazy loading and eager loading in ORM and demonstrate their application in SQLAlchemy.


#### Advanced SQL Querying

* **JOINS**: Allow us to utilize the relationships between tables and query information from multiple tables at a time so long as they share relationships.
![join_pic](https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Screenshots/DE-SQL-Join-Typen.png)
    * **INNER JOIN**: Grabs overlapping information from two tables. (Entry from one table has to be connected to an entry from the other. If an item is not connected to and item from the other it is not included)
    * **LEFT JOIN**: Grabs all the information that is overlapping, aswell as any non connected items from the 'left' table (the starting table).
    * **RIGHT JOIN**: Grabs all the information that is overlapping, aswell as any non connected items from the 'right' table (the table we are joining to).
    * **FULL OUTER JOIN**: Grabs all info connect or not from both tables.

#### ORM Advanced Querying with SQLAlchemy

We can take alot of these querying principles and further enhance the API we have been working on.

- Filtering products using .where(), filter(), filter_by() and a query parameter search term
- Linking orders to products using our products attribute and Nested Schemas .join()
- Searching for order by order_id
- Searching for orders by customer_id
- Searching for orders by customer_name

##### We'll also discuss the concept of 'Lazy' vs 'Eager' loading:

- Lazy: When we access a relation ship from table1 to table2, only the data from table2 is loaded, and the table1 associate is not

- Eager: Now when accessing a relationship, SQL issues two separate SELECT queries to gather the info from both tables.


#### Pagination:
Pagination allows for optimization when dealing with large datasets. With pagination we are able to carve our data into condensed packages determined by the end user.
