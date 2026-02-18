-- Renomeando tabelas de Fatos
EXEC sp_rename 'FactSales', 'FatoVendas';
EXEC sp_rename 'FactInventory', 'FatoInventario';
EXEC sp_rename 'FactOnlineSales', 'FatoVendasOnline';
EXEC sp_rename 'FactExchangeRate', 'FatoTaxaCambio';

-- Renomeando tabelas de Dimensões
EXEC sp_rename 'DimCustomer', 'DimCliente';
EXEC sp_rename 'DimProduct', 'DimProduto';
EXEC sp_rename 'DimDate', 'DimData';
EXEC sp_rename 'DimGeography', 'DimGeografia';
EXEC sp_rename 'DimCurrency', 'DimMoeda';
EXEC sp_rename 'DimPromotion', 'DimPromocao';
EXEC sp_rename 'DimStore', 'DimLoja';
EXEC sp_rename 'DimScenario', 'DimCenario';
EXEC sp_rename 'DimSalesTerritory', 'DimTerritorioVendas';
