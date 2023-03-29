-- Table: public.tasks

-- DROP TABLE IF EXISTS public.tasks;

CREATE TABLE IF NOT EXISTS public.tasks
(
    id serial PRIMARY KEY,
    name character varying COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    due_date date
);

-- Grant necessary access to the user
GRANT ALL PRIVILEGES ON TABLE public.tasks TO your_actual_db_user;
