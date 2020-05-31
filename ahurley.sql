DROP TABLE IF EXISTS public.journal;
DROP TABLE IF EXISTS public.rooms;

CREATE TABLE public.rooms (
    id SERIAL PRIMARY KEY,
    name character varying NOT NULL UNIQUE,
    count integer NOT NULL DEFAULT 0,
    lat float,
    lon float
);

CREATE TABLE public.journal (
    id SERIAL PRIMARY KEY,
    room_id integer NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    previous_count integer DEFAULT 0,
    count integer NOT NULL DEFAULT 0,
    delta integer GENERATED ALWAYS AS (count - COALESCE(previous_count, 0)) STORED,
    applied_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION update_journal_record() RETURNS trigger AS $journal_stamp$
    BEGIN
        INSERT INTO public.JOURNAL (room_id, previous_count, count) VALUES (NEW.id, OLD.count, NEW.count);

        IF NEW.count IS NULL THEN
            RAISE EXCEPTION 'count cannot be null';
        END IF;

        IF NEW.count < 0 THEN
            RAISE EXCEPTION '% cannot have a negative count', NEW.id;
        END IF;

        RETURN NEW;
    END;
$journal_stamp$ LANGUAGE plpgsql;

CREATE TRIGGER update_journal
    AFTER UPDATE OR INSERT ON public.rooms
    FOR EACH ROW
    EXECUTE PROCEDURE update_journal_record();

INSERT INTO rooms (name,lon,lat) VALUES ('Little Ceasars', -83.4961, 42.2738);
INSERT INTO rooms (name,lon,lat) VALUES ('Pet Supplies Plus', -83.5735113, 42.360868);
INSERT INTO rooms (name,lon,lat) VALUES ('Tractor Supply Co', -83.6240911, 42.3630711);

UPDATE ROOMS SET count=3 WHERE name = 'Little Ceasars';
UPDATE ROOMS SET count=12 WHERE name = 'Pet Supplies Plus';
UPDATE ROOMS SET count=7 WHERE name = 'Tractor Supply Co';

