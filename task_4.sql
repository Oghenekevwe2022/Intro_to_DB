USE alx_book_store;
SELECT
    COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'Books'
    AND "TABLE_SCHEMA = 'alx_book_store'"