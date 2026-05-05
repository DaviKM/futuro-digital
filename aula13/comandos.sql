-- Table: public.produto

-- DROP TABLE IF EXISTS public.produto;

CREATE TABLE IF NOT EXISTS public.produto
(
    nome character varying COLLATE pg_catalog."default",
    id_produto bigint NOT NULL DEFAULT nextval('produto_id_produto_seq'::regclass),
    preco numeric(10,2),
    categoria character varying COLLATE pg_catalog."default",
    CONSTRAINT produto_pkey PRIMARY KEY (id_produto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.produto
    OWNER to postgres;