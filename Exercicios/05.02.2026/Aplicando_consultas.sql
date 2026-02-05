-- Cadastro dos Clientes
select * from clientes;

-- Cadastro dos Produtos
select * from produtos;

-- Cadastro dos Itens Pedidos
select * from itens_pedido;

-- Cadastro dos Pedidos
select * from pedidos;

select avg(valor_total) from pedidos;-- Media dos Valores
select sum(valor_total) from pedidos; -- Soma dos Valores
select max(valor_total) from pedidos; -- Maior Valor
select min(valor_total) from pedidos; -- Menor Valor

select *
from clientes as cli
inner join pedidos as ped
on cli.cliente_id = ped.cliente_id
ORDER BY ped.data_pedido; -- Ordenação

-- Filtros
-- WHERE ped.data_pedido >= '2026-01-01'
-- AND cli.estado = 'SP';