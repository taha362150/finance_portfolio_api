CREATE DATABASE FinanceDB;
----------------------------------------------------------------------------

GO
USE FinanceDB;

----------------------------------------------------------------------------
CREATE TABLE Clients (
	client_id INT IDENTITY PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100)
);

CREATE TABLE Assets (
	asset_id INT IDENTITY PRIMARY KEY,
	name VARCHAR(100),
	asset_type VARCHAR(50),
	current_price FLOAT
);

CREATE TABLE Portfolios (
    portfolio_id INT IDENTITY PRIMARY KEY,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

CREATE TABLE Transactions (
    transaction_id INT IDENTITY PRIMARY KEY,
    portfolio_id INT,
    asset_id INT,
    quantity INT,
    price FLOAT,
    transaction_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);
