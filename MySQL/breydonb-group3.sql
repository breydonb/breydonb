SELECT vendor_name,vendor_contact_last_name, vendor_contact_first_name FROM VENDORS 
    ORDER BY vendor_contact_last_name, vendor_contact_first_name;

SELECT vendor_contact_last_name || ', ' || vendor_contact_first_name as full_name FROM VENDORS 
    WHERE vendor_contact_last_name < 'D' OR vendor_contact_last_name = 'E';

SELECT invoice_due_date AS "Due Date", invoice_total AS "Invoice Total", (invoice_total * .1) AS "10%", (invoice_total * 1.1) AS "Plus 10%" FROM INVOICES
    WHERE invoice_total >= 500 AND invoice_total <= 1000 
    ORDER BY invoice_due_date DESC;
    
SELECT (invoice_total - payment_total - credit_total) AS "Balance Due", payment_date AS "Payment Date" from invoices
    WHERE payment_date is null AND (invoice_total - payment_total - credit_total) = 0;


