--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: arquivo_cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.arquivo_cliente (
    id integer NOT NULL,
    arquivo character varying NOT NULL,
    "idCliente" integer
);


ALTER TABLE public.arquivo_cliente OWNER TO postgres;

--
-- Name: arquivo_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.arquivo_cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arquivo_cliente_id_seq OWNER TO postgres;

--
-- Name: arquivo_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.arquivo_cliente_id_seq OWNED BY public.arquivo_cliente.id;


--
-- Name: arquivo_oficina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.arquivo_oficina (
    id integer NOT NULL,
    arquivo character varying NOT NULL,
    "idOficina" integer
);


ALTER TABLE public.arquivo_oficina OWNER TO postgres;

--
-- Name: arquivo_oficina_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.arquivo_oficina_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arquivo_oficina_id_seq OWNER TO postgres;

--
-- Name: arquivo_oficina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.arquivo_oficina_id_seq OWNED BY public.arquivo_oficina.id;


--
-- Name: avaliacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.avaliacao (
    id integer NOT NULL,
    nota integer NOT NULL,
    comentario character varying NOT NULL,
    "idCliente" integer,
    "idOficina" integer
);


ALTER TABLE public.avaliacao OWNER TO postgres;

--
-- Name: avaliacao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.avaliacao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avaliacao_id_seq OWNER TO postgres;

--
-- Name: avaliacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.avaliacao_id_seq OWNED BY public.avaliacao.id;


--
-- Name: cartao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cartao (
    id integer NOT NULL,
    pan bigint NOT NULL,
    "dataValidade" character varying NOT NULL,
    "codigoSeguranca" integer NOT NULL,
    "nomeCartao" character varying NOT NULL,
    "idCliente" integer
);


ALTER TABLE public.cartao OWNER TO postgres;

--
-- Name: cartao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cartao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cartao_id_seq OWNER TO postgres;

--
-- Name: cartao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cartao_id_seq OWNED BY public.cartao.id;


--
-- Name: chat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chat (
    id integer NOT NULL,
    "idCliente" integer,
    "idOficina" integer
);


ALTER TABLE public.chat OWNER TO postgres;

--
-- Name: chat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_id_seq OWNER TO postgres;

--
-- Name: chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chat_id_seq OWNED BY public.chat.id;


--
-- Name: chat_mensagem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chat_mensagem (
    id integer NOT NULL,
    mensagem character varying NOT NULL,
    data integer NOT NULL,
    receptor character varying NOT NULL,
    emissor character varying NOT NULL,
    "idCliente" integer
);


ALTER TABLE public.chat_mensagem OWNER TO postgres;

--
-- Name: chat_mensagem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chat_mensagem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_mensagem_id_seq OWNER TO postgres;

--
-- Name: chat_mensagem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chat_mensagem_id_seq OWNED BY public.chat_mensagem.id;


--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    telefone integer NOT NULL,
    aniversario character varying NOT NULL,
    email character varying(50) NOT NULL,
    senha character varying(50) NOT NULL,
    autenticado boolean,
    "dataCadastro" character varying,
    raio integer
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cliente_id_seq OWNER TO postgres;

--
-- Name: cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cliente_id_seq OWNED BY public.cliente.id;


--
-- Name: endereco; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.endereco (
    id integer NOT NULL,
    latitude double precision NOT NULL,
    longitude double precision NOT NULL,
    cep integer NOT NULL,
    numero integer NOT NULL,
    "idOficina" integer
);


ALTER TABLE public.endereco OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.endereco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.endereco_id_seq OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.endereco_id_seq OWNED BY public.endereco.id;


--
-- Name: item_ordem_servico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.item_ordem_servico (
    id integer NOT NULL,
    "qntProduto" integer NOT NULL,
    "idOrdemServico" integer,
    "idProduto" integer
);


ALTER TABLE public.item_ordem_servico OWNER TO postgres;

--
-- Name: item_ordem_servico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.item_ordem_servico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_ordem_servico_id_seq OWNER TO postgres;

--
-- Name: item_ordem_servico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.item_ordem_servico_id_seq OWNED BY public.item_ordem_servico.id;


--
-- Name: oficina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oficina (
    id integer NOT NULL,
    nome character varying NOT NULL,
    email character varying NOT NULL,
    senha character varying NOT NULL,
    "cpfCnpj" character varying NOT NULL,
    "avaliacaoTotal" double precision,
    descricao character varying,
    "dataCadastro" character varying,
    "qntOrcamentosAtendidos" integer,
    "qntOrcamentosRejeitados" integer,
    "qntReboquesAtendidos" integer,
    "qntReboquesRejeitados" integer,
    "horarioFuncionamento" character varying NOT NULL
);


ALTER TABLE public.oficina OWNER TO postgres;

--
-- Name: oficina_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oficina_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oficina_id_seq OWNER TO postgres;

--
-- Name: oficina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oficina_id_seq OWNED BY public.oficina.id;


--
-- Name: ordem_servico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ordem_servico (
    id integer NOT NULL,
    data integer NOT NULL,
    status boolean NOT NULL,
    "precoTotal" double precision NOT NULL,
    "idCliente" integer,
    "idOficina" integer
);


ALTER TABLE public.ordem_servico OWNER TO postgres;

--
-- Name: ordem_servico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ordem_servico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ordem_servico_id_seq OWNER TO postgres;

--
-- Name: ordem_servico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ordem_servico_id_seq OWNED BY public.ordem_servico.id;


--
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    id integer NOT NULL,
    nome character varying NOT NULL,
    preco double precision NOT NULL,
    descricao character varying NOT NULL,
    categoria character varying NOT NULL,
    "precoCancelamento" double precision NOT NULL,
    "idOficina" integer
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- Name: produto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produto_id_seq OWNER TO postgres;

--
-- Name: produto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produto_id_seq OWNED BY public.produto.id;


--
-- Name: arquivo_cliente id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_cliente ALTER COLUMN id SET DEFAULT nextval('public.arquivo_cliente_id_seq'::regclass);


--
-- Name: arquivo_oficina id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_oficina ALTER COLUMN id SET DEFAULT nextval('public.arquivo_oficina_id_seq'::regclass);


--
-- Name: avaliacao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao ALTER COLUMN id SET DEFAULT nextval('public.avaliacao_id_seq'::regclass);


--
-- Name: cartao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cartao ALTER COLUMN id SET DEFAULT nextval('public.cartao_id_seq'::regclass);


--
-- Name: chat id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat ALTER COLUMN id SET DEFAULT nextval('public.chat_id_seq'::regclass);


--
-- Name: chat_mensagem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_mensagem ALTER COLUMN id SET DEFAULT nextval('public.chat_mensagem_id_seq'::regclass);


--
-- Name: cliente id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente ALTER COLUMN id SET DEFAULT nextval('public.cliente_id_seq'::regclass);


--
-- Name: endereco id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco ALTER COLUMN id SET DEFAULT nextval('public.endereco_id_seq'::regclass);


--
-- Name: item_ordem_servico id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_ordem_servico ALTER COLUMN id SET DEFAULT nextval('public.item_ordem_servico_id_seq'::regclass);


--
-- Name: oficina id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oficina ALTER COLUMN id SET DEFAULT nextval('public.oficina_id_seq'::regclass);


--
-- Name: ordem_servico id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem_servico ALTER COLUMN id SET DEFAULT nextval('public.ordem_servico_id_seq'::regclass);


--
-- Name: produto id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto ALTER COLUMN id SET DEFAULT nextval('public.produto_id_seq'::regclass);


--
-- Name: arquivo_cliente arquivo_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_cliente
    ADD CONSTRAINT arquivo_cliente_pkey PRIMARY KEY (id);


--
-- Name: arquivo_oficina arquivo_oficina_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_oficina
    ADD CONSTRAINT arquivo_oficina_pkey PRIMARY KEY (id);


--
-- Name: avaliacao avaliacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao
    ADD CONSTRAINT avaliacao_pkey PRIMARY KEY (id);


--
-- Name: cartao cartao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cartao
    ADD CONSTRAINT cartao_pkey PRIMARY KEY (id);


--
-- Name: chat_mensagem chat_mensagem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_mensagem
    ADD CONSTRAINT chat_mensagem_pkey PRIMARY KEY (id);


--
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (id);


--
-- Name: cliente cliente_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_email_key UNIQUE (email);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);


--
-- Name: endereco endereco_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pkey PRIMARY KEY (id);


--
-- Name: item_ordem_servico item_ordem_servico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_ordem_servico
    ADD CONSTRAINT item_ordem_servico_pkey PRIMARY KEY (id);


--
-- Name: oficina oficina_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oficina
    ADD CONSTRAINT oficina_email_key UNIQUE (email);


--
-- Name: oficina oficina_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oficina
    ADD CONSTRAINT oficina_pkey PRIMARY KEY (id);


--
-- Name: ordem_servico ordem_servico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem_servico
    ADD CONSTRAINT ordem_servico_pkey PRIMARY KEY (id);


--
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id);


--
-- Name: arquivo_cliente arquivo_cliente_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_cliente
    ADD CONSTRAINT "arquivo_cliente_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.cliente(id);


--
-- Name: arquivo_oficina arquivo_oficina_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arquivo_oficina
    ADD CONSTRAINT "arquivo_oficina_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- Name: avaliacao avaliacao_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao
    ADD CONSTRAINT "avaliacao_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.cliente(id);


--
-- Name: avaliacao avaliacao_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao
    ADD CONSTRAINT "avaliacao_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- Name: cartao cartao_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cartao
    ADD CONSTRAINT "cartao_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.cliente(id);


--
-- Name: chat chat_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT "chat_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.cliente(id);


--
-- Name: chat chat_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT "chat_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- Name: chat_mensagem chat_mensagem_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_mensagem
    ADD CONSTRAINT "chat_mensagem_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.chat(id);


--
-- Name: endereco endereco_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT "endereco_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- Name: item_ordem_servico item_ordem_servico_idOrdemServico_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_ordem_servico
    ADD CONSTRAINT "item_ordem_servico_idOrdemServico_fkey" FOREIGN KEY ("idOrdemServico") REFERENCES public.ordem_servico(id);


--
-- Name: item_ordem_servico item_ordem_servico_idProduto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_ordem_servico
    ADD CONSTRAINT "item_ordem_servico_idProduto_fkey" FOREIGN KEY ("idProduto") REFERENCES public.produto(id);


--
-- Name: ordem_servico ordem_servico_idCliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem_servico
    ADD CONSTRAINT "ordem_servico_idCliente_fkey" FOREIGN KEY ("idCliente") REFERENCES public.cliente(id);


--
-- Name: ordem_servico ordem_servico_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ordem_servico
    ADD CONSTRAINT "ordem_servico_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- Name: produto produto_idOficina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT "produto_idOficina_fkey" FOREIGN KEY ("idOficina") REFERENCES public.oficina(id);


--
-- PostgreSQL database dump complete
--

