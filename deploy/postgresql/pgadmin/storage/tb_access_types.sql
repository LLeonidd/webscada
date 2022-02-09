--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1

-- Started on 2022-01-26 21:40:44 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 211 (class 1259 OID 16392)
-- Name: tb_access_types; Type: TABLE; Schema: public; Owner: admin_user
--

CREATE TABLE public.tb_access_types (
    id bigint NOT NULL,
    name character varying(228) NOT NULL,
    description character varying(228) NOT NULL
);


ALTER TABLE public.tb_access_types OWNER TO admin_user;

--
-- TOC entry 212 (class 1259 OID 16395)
-- Name: tb_access_types_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_user
--

CREATE SEQUENCE public.tb_access_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tb_access_types_id_seq OWNER TO admin_user;

--
-- TOC entry 3327 (class 0 OID 0)
-- Dependencies: 212
-- Name: tb_access_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_user
--

ALTER SEQUENCE public.tb_access_types_id_seq OWNED BY public.tb_access_types.id;


--
-- TOC entry 3178 (class 2604 OID 16406)
-- Name: tb_access_types id; Type: DEFAULT; Schema: public; Owner: admin_user
--

ALTER TABLE ONLY public.tb_access_types ALTER COLUMN id SET DEFAULT nextval('public.tb_access_types_id_seq'::regclass);


--
-- TOC entry 3320 (class 0 OID 16392)
-- Dependencies: 211
-- Data for Name: tb_access_types; Type: TABLE DATA; Schema: public; Owner: admin_user
--

COPY public.tb_access_types (id, name, description) FROM stdin;
1	R	Read
2	R/W	Read/Write
\.


--
-- TOC entry 3328 (class 0 OID 0)
-- Dependencies: 212
-- Name: tb_access_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_user
--

SELECT pg_catalog.setval('public.tb_access_types_id_seq', 2, true);


--
-- TOC entry 3180 (class 2606 OID 16398)
-- Name: tb_access_types tb_access_types_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_user
--

ALTER TABLE ONLY public.tb_access_types
    ADD CONSTRAINT tb_access_types_pkey PRIMARY KEY (id);


-- Completed on 2022-01-26 21:40:44 UTC

--
-- PostgreSQL database dump complete
--

