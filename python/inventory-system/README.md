# 📦 Inventory Management System

> A practical console-based application for managing product inventory with real-time stock tracking.

---

## 🎯 Project Overview

This project is a **command-line inventory management system** designed to handle basic warehouse operations. It demonstrates proficiency in:

- **Data Structures:** Using dictionaries and lists to organize product information
- **Control Flow:** Implementing menus and conditional logic
- **Input Validation:** Ensuring data integrity through user input validation
- **Error Handling:** Graceful handling of edge cases (insufficient stock, product not found)
- **User Interaction:** Creating intuitive CLI interfaces

---

## ✨ Features

### 1. View Inventory
Displays all products with their current stock levels and prices in a formatted table.

```
Nome: Tomate | Qtd: 4 | Preço: R$ 12.99
Nome: Banana | Qtd: 8 | Preço: R$ 10.90
Nome: Laranja | Qtd: 10 | Preço: R$ 14.75
```

### 2. Register Entry
Add stock to existing products with automatic quantity updates.
- Validates product existence
- Accepts only numeric input
- Updates inventory in real-time

### 3. Register Removal
Remove stock from products with built-in safety checks.
- Validates product existence
- Checks for sufficient inventory
- Prevents negative stock situations
- Accepts only numeric input

### 4. Exit System
Gracefully closes the application.

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- No external dependencies required

### Installation

```bash
# Clone the repository
git clone https://github.com/rafaeldominguess/estudos.git

# Navigate to the project
cd estudos/python/inventory-system
```

### Running the Application

```bash
python main.py
```

---

## 📋 Usage Examples

### Starting the Application
```bash
$ python main.py
Escolha uma das opções:
1 - Visualizar Estoque Atual
2 - Registrar Entrada de Produto
3 - Registrar Saída de Produto
4 - Sair do Sistema
Digite sua escolha:
```

### Viewing Inventory (Option 1)
```
Digite sua escolha: 1
Nome: Tomate | Qtd: 4 | Preço: R$ 12.99
Nome: Banana | Qtd: 8 | Preço: R$ 10.90
Nome: Laranja | Qtd: 10 | Preço: R$ 14.75
```

### Registering Entry (Option 2)
```
Digite sua escolha: 2
Digite o nome do produto: Tomate
Digite a quantidade: 5
Entrada registrada!
```

### Registering Removal (Option 3)
```
Digite sua escolha: 3
Digite o nome do produto: Banana
Digite a quantidade a remover: 2
Saída registrada!
```

---

## 🏗️ Code Structure

```
inventory-system/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies (if any)
└── README.md           # This file
```

---

## 💡 Key Concepts Demonstrated

### Data Structures
```python
# List of dictionaries for flexible product management
estoque = [
    {"nome": "Tomate", "quantidade": 4, "preco": 12.99},
    {"nome": "Banana", "quantidade": 8, "preco": 10.90}
]
```

### Input Validation
```python
# Ensures only numeric input is accepted
if quantidade_solicitada.isdigit():
    quantidade_solicitada = int(quantidade_solicitada)
```

### Business Logic
```python
# Prevents selling more than available
if quantidade_solicitada <= produto["quantidade"]:
    produto["quantidade"] -= quantidade_solicitada
else:
    print("Estoque insuficiente")
```

---

## 🔄 Future Improvements

Potential enhancements for version 2.0:
- [ ] File persistence (save/load inventory from file)
- [ ] Database integration (SQLite/MySQL)
- [ ] GUI interface (PyQt/Tkinter)
- [ ] Product categories
- [ ] Transaction history
- [ ] Automated alerts for low stock
- [ ] Price update functionality
- [ ] Multi-user support

---

## 📝 License

This project is part of my learning journey and study portfolio.

---

## 👨‍💻 Author

**Rafael Dominguess**
- GitHub: [@rafaeldominguess](https://github.com/rafaeldominguess)
- Portfolio: [estudos](https://github.com/rafaeldominguess/estudos)

---

**Created:** May 2026
**Status:** ✅ Complete and Functional
