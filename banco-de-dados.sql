--
-- PostgreSQL database dump
--

\restrict 9hBTLa78ainNsauStfnEkoyW6ePdq0R4qsJ9P2gMXSJ68Khh5lXkWLTrm8MIXOg

-- Dumped from database version 18.4 (Ubuntu 18.4-1.pgdg24.04+1)
-- Dumped by pg_dump version 18.4 (Ubuntu 18.4-1.pgdg24.04+1)

-- Started on 2026-05-24 17:01:39 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE loja;
--
-- TOC entry 3507 (class 1262 OID 16384)
-- Name: loja; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE loja WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'pt_BR.UTF-8';


ALTER DATABASE loja OWNER TO postgres;

\unrestrict 9hBTLa78ainNsauStfnEkoyW6ePdq0R4qsJ9P2gMXSJ68Khh5lXkWLTrm8MIXOg
\connect loja
\restrict 9hBTLa78ainNsauStfnEkoyW6ePdq0R4qsJ9P2gMXSJ68Khh5lXkWLTrm8MIXOg

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 219 (class 1259 OID 16385)
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    nome_cliente character varying,
    email character varying,
    cidade character varying,
    id bigint NOT NULL
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16391)
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clientes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO postgres;

--
-- TOC entry 3508 (class 0 OID 0)
-- Dependencies: 220
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- TOC entry 221 (class 1259 OID 16392)
-- Name: itens_compra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.itens_compra (
    pedido_id bigint NOT NULL,
    produto_id bigint NOT NULL,
    quantidade integer,
    preco_unitario numeric(10,2)
);


ALTER TABLE public.itens_compra OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16397)
-- Name: marcas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.marcas (
    nome_marca character varying,
    pais_origem character varying,
    id bigint NOT NULL
);


ALTER TABLE public.marcas OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16403)
-- Name: marcas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.marcas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.marcas_id_seq OWNER TO postgres;

--
-- TOC entry 3509 (class 0 OID 0)
-- Dependencies: 223
-- Name: marcas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.marcas_id_seq OWNED BY public.marcas.id;


--
-- TOC entry 224 (class 1259 OID 16404)
-- Name: pedidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedidos (
    id bigint NOT NULL,
    cliente_id bigint,
    data_pedido timestamp without time zone,
    status character varying
);


ALTER TABLE public.pedidos OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16410)
-- Name: pedidos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedidos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pedidos_id_seq OWNER TO postgres;

--
-- TOC entry 3510 (class 0 OID 0)
-- Dependencies: 225
-- Name: pedidos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedidos_id_seq OWNED BY public.pedidos.id;


--
-- TOC entry 226 (class 1259 OID 16411)
-- Name: produtos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtos (
    id bigint NOT NULL,
    nome_produto character varying,
    preco numeric(10,2),
    estoque integer,
    marca_id bigint
);


ALTER TABLE public.produtos OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16417)
-- Name: produtos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produtos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.produtos_id_seq OWNER TO postgres;

--
-- TOC entry 3511 (class 0 OID 0)
-- Dependencies: 227
-- Name: produtos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produtos_id_seq OWNED BY public.produtos.id;


--
-- TOC entry 3328 (class 2604 OID 16418)
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- TOC entry 3329 (class 2604 OID 16419)
-- Name: marcas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcas ALTER COLUMN id SET DEFAULT nextval('public.marcas_id_seq'::regclass);


--
-- TOC entry 3330 (class 2604 OID 16420)
-- Name: pedidos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos ALTER COLUMN id SET DEFAULT nextval('public.pedidos_id_seq'::regclass);


--
-- TOC entry 3331 (class 2604 OID 16421)
-- Name: produtos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos ALTER COLUMN id SET DEFAULT nextval('public.produtos_id_seq'::regclass);


--
-- TOC entry 3493 (class 0 OID 16385)
-- Dependencies: 219
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.clientes VALUES ('Alice Lima', 'alice@email.com', 'São Paulo', 1);
INSERT INTO public.clientes VALUES ('Bruno Costa', 'bruno@email.com', 'Rio de Janeiro', 2);
INSERT INTO public.clientes VALUES ('Carla Diniz', 'carla@email.com', 'Belo Horizonte', 3);
INSERT INTO public.clientes VALUES ('David Rocha', 'david@email.com', 'São Paulo', 4);
INSERT INTO public.clientes VALUES ('davizusch', 'emailzinho', 'canoas', 5);


--
-- TOC entry 3495 (class 0 OID 16392)
-- Dependencies: 221
-- Data for Name: itens_compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.itens_compra VALUES (1, 1, 1, 1200.00);
INSERT INTO public.itens_compra VALUES (1, 4, 2, 450.00);
INSERT INTO public.itens_compra VALUES (2, 3, 1, 3500.00);
INSERT INTO public.itens_compra VALUES (3, 2, 5, 250.50);
INSERT INTO public.itens_compra VALUES (4, 5, 1, 89.90);
INSERT INTO public.itens_compra VALUES (4, 6, 1, 199.90);


--
-- TOC entry 3496 (class 0 OID 16397)
-- Dependencies: 222
-- Data for Name: marcas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.marcas VALUES ('TechMaster', 'Estados Unidos', 1);
INSERT INTO public.marcas VALUES ('CasaPlus', 'Alemanha', 2);
INSERT INTO public.marcas VALUES ('SoundBeat', 'Japão', 3);
INSERT INTO public.marcas VALUES ('StyleWear', 'Brasil', 4);


--
-- TOC entry 3498 (class 0 OID 16404)
-- Dependencies: 224
-- Data for Name: pedidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pedidos VALUES (1, 1, '2025-09-01 00:00:00', 'Entregue');
INSERT INTO public.pedidos VALUES (2, 2, '2025-09-05 00:00:00', 'Enviado');
INSERT INTO public.pedidos VALUES (3, 1, '2025-09-10 00:00:00', 'Processando');
INSERT INTO public.pedidos VALUES (4, 3, '2025-09-15 00:00:00', 'Entregue');


--
-- TOC entry 3500 (class 0 OID 16411)
-- Dependencies: 226
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.produtos VALUES (1, 'Smartphone X1', 1200.00, 15, 1);
INSERT INTO public.produtos VALUES (2, 'Headphone Pro', 250.50, 30, 3);
INSERT INTO public.produtos VALUES (3, 'Geladeira Frost', 3500.00, 8, 2);
INSERT INTO public.produtos VALUES (4, 'Máquina de Café', 450.00, 20, 2);
INSERT INTO public.produtos VALUES (5, 'Camiseta Casual', 89.90, 50, 4);
INSERT INTO public.produtos VALUES (6, 'Tênis Esportivo', 199.90, 25, 4);


--
-- TOC entry 3512 (class 0 OID 0)
-- Dependencies: 220
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clientes_id_seq', 5, true);


--
-- TOC entry 3513 (class 0 OID 0)
-- Dependencies: 223
-- Name: marcas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.marcas_id_seq', 1, false);


--
-- TOC entry 3514 (class 0 OID 0)
-- Dependencies: 225
-- Name: pedidos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedidos_id_seq', 1, false);


--
-- TOC entry 3515 (class 0 OID 0)
-- Dependencies: 227
-- Name: produtos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produtos_id_seq', 1, false);


--
-- TOC entry 3333 (class 2606 OID 16423)
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- TOC entry 3335 (class 2606 OID 16425)
-- Name: itens_compra itens_compra_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_compra
    ADD CONSTRAINT itens_compra_id PRIMARY KEY (pedido_id, produto_id);


--
-- TOC entry 3337 (class 2606 OID 16427)
-- Name: marcas marcas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marcas
    ADD CONSTRAINT marcas_pkey PRIMARY KEY (id);


--
-- TOC entry 3339 (class 2606 OID 16429)
-- Name: pedidos pedidos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY (id);


--
-- TOC entry 3341 (class 2606 OID 16431)
-- Name: produtos produtos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pkey PRIMARY KEY (id);


--
-- TOC entry 3344 (class 2606 OID 16432)
-- Name: pedidos cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT cliente_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3345 (class 2606 OID 16437)
-- Name: produtos marcas_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT marcas_fkey FOREIGN KEY (marca_id) REFERENCES public.marcas(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3342 (class 2606 OID 16442)
-- Name: itens_compra pedido_Fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_compra
    ADD CONSTRAINT "pedido_Fkey" FOREIGN KEY (pedido_id) REFERENCES public.pedidos(id);


--
-- TOC entry 3343 (class 2606 OID 16447)
-- Name: itens_compra produto_Fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.itens_compra
    ADD CONSTRAINT "produto_Fkey" FOREIGN KEY (produto_id) REFERENCES public.produtos(id);


-- Completed on 2026-05-24 17:01:39 -03

--
-- PostgreSQL database dump complete
--

\unrestrict 9hBTLa78ainNsauStfnEkoyW6ePdq0R4qsJ9P2gMXSJ68Khh5lXkWLTrm8MIXOg

