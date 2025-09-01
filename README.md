# Proyecto Python MySQL - Introducción Completa

Este proyecto es una **introducción progresiva al desarrollo con Python**, que abarca desde conceptos básicos hasta la gestión de bases de datos MySQL. Está diseñado como un curso práctico que guía al estudiante a través de diferentes etapas de complejidad creciente.

## 📋 Descripción del Proyecto

Este proyecto demuestra la evolución natural del desarrollo en Python, comenzando con conceptos fundamentales y avanzando hacia aplicaciones más complejas que involucran:

- **Programación básica** con menús interactivos
- **Manejo de archivos CSV** con pandas
- **Conexión y gestión de bases de datos MySQL**
- **Arquitectura modular** y buenas prácticas de programación
- **Visualización de datos** con matplotlib

## 🗂️ Estructura del Proyecto

### Etapa 1: Programación Básica
**📁 `etapa1-soloMenu/`**
- `menu.py`: Menú interactivo básico con opciones simples
- **Objetivo**: Introducir conceptos de control de flujo, bucles y entrada de usuario

### Etapa 2: Funciones y Módulos
**📁 `etapa2-Menu_Funciones_y_Modulos/`**
- `1_menu_funcion_intro.py`: Introducción a funciones
- `2_menu_y_funciones.py`: Menú con funciones organizadas
- `3_modulo/`: Implementación modular con archivos separados
- **Objetivo**: Aprender a organizar código en funciones y módulos reutilizables

### Etapa 3: Conexión a Base de Datos
**📁 `etapa3-conexionBD_MySQL/`**
- `conexion_mysql.py`: Configuración básica de conexión MySQL
- **Objetivo**: Establecer conexión con base de datos MySQL

### Etapa 4: CRUD Completo
**📁 `etapa4-menu_modularizado_crud_mysql/`**
- `menu.py`: Menú principal del sistema CRUD
- `baseDeDatos.py`: Módulo de conexión a base de datos
- `crudPersona.py`: Operaciones CRUD para personas
- `crudCiudad.py`: Operaciones CRUD para ciudades
- `sql/script.sql`: Scripts de creación de base de datos
- **Objetivo**: Implementar un sistema completo de gestión de datos

### Etapa CSV: Manejo de Datos
**📁 `etapa_csv/`**
- `horarios.csv`: Archivo de datos de ejemplo
- `horarios.py`: Lectura y procesamiento de CSV con pandas
- **Objetivo**: Aprender a trabajar con archivos CSV y la librería pandas

### Etapa CSV-MySQL: Integración
**📁 `etapa_csv_mysql/`**
- `csv_to_mysql.py`: Importación de datos CSV a MySQL
- `horariosMySQL.csv`: Datos para importar
- `script.sql`: Scripts de base de datos
- **Objetivo**: Integrar datos CSV con base de datos MySQL

### Etapa Gráficos: Visualización
**📁 `etapa_graficos_matplotlib/`**
- **Objetivo**: Crear visualizaciones de datos con matplotlib

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **MySQL**: Base de datos relacional
- **pandas**: Manipulación y análisis de datos
- **matplotlib**: Visualización de datos
- **mysql-connector-python**: Conector para MySQL

## 📦 Dependencias

El archivo `requirements.txt` contiene todas las dependencias necesarias:

```
mysql-connector
mysql-connector-python
pandas
matplotlib
```

---

# 🐍 Guía Completa de Entornos Virtuales en Python

## ¿Qué son los Entornos Virtuales?

Un **entorno virtual** es un directorio aislado que contiene una instalación específica de Python y sus paquetes. Permite:

- ✅ **Aislar dependencias** entre diferentes proyectos
- ✅ **Evitar conflictos** de versiones de paquetes
- ✅ **Mantener el sistema limpio** sin instalar paquetes globalmente
- ✅ **Facilitar el despliegue** y la distribución de proyectos
- ✅ **Permitir diferentes versiones** de Python para cada proyecto

## 🐧 Uso en Linux

### 1. Crear un Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv nombre_del_entorno

# Ejemplo específico para este proyecto
python3 -m venv mientorno
```

### 2. Activar el Entorno Virtual

```bash
# Activar el entorno virtual
source nombre_del_entorno/bin/activate

# Para este proyecto
source mientorno/bin/activate
```

**Indicador visual**: Cuando está activado, verás `(nombre_del_entorno)` al inicio de tu prompt:
```bash
(mientorno) usuario@servidor:~/proyecto$
```

### 3. Instalar Dependencias

```bash
# Instalar desde requirements.txt
pip install -r requirements.txt

# O instalar paquetes individuales
pip install pandas matplotlib mysql-connector-python
```

### 4. Verificar Paquetes Instalados

```bash
# Ver todos los paquetes instalados
pip list

# Ver paquetes con versiones específicas
pip freeze
```

### 5. Generar requirements.txt

```bash
# Crear/actualizar requirements.txt con paquetes actuales
pip freeze > requirements.txt
```

### 6. Desactivar el Entorno Virtual

```bash
# Desactivar el entorno virtual
deactivate
```

## 🪟 Uso en Windows

### 1. Crear un Entorno Virtual

```cmd
# Crear entorno virtual
python -m venv nombre_del_entorno

# Ejemplo específico para este proyecto
python -m venv mientorno
```

### 2. Activar el Entorno Virtual

```cmd
# En Command Prompt (cmd)
nombre_del_entorno\Scripts\activate

# En PowerShell
nombre_del_entorno\Scripts\Activate.ps1

# Para este proyecto
mientorno\Scripts\activate
```

**Indicador visual**: Cuando está activado, verás `(nombre_del_entorno)` al inicio de tu prompt:
```cmd
(mientorno) C:\ruta\al\proyecto>
```

### 3. Instalar Dependencias

```cmd
# Instalar desde requirements.txt
pip install -r requirements.txt

# O instalar paquetes individuales
pip install pandas matplotlib mysql-connector-python
```

### 4. Verificar Paquetes Instalados

```cmd
# Ver todos los paquetes instalados
pip list

# Ver paquetes con versiones específicas
pip freeze
```

### 5. Generar requirements.txt

```cmd
# Crear/actualizar requirements.txt con paquetes actuales
pip freeze > requirements.txt
```

### 6. Desactivar el Entorno Virtual

```cmd
# Desactivar el entorno virtual
deactivate
```

## 🔧 Comandos Útiles Adicionales

### Gestión de Entornos Virtuales

```bash
# Ver la ubicación del Python del entorno virtual
which python  # Linux/Mac
where python  # Windows

# Ver la versión de Python
python --version

# Actualizar pip
pip install --upgrade pip

# Instalar un paquete en modo desarrollo
pip install -e .

# Desinstalar un paquete
pip uninstall nombre_del_paquete
```

### Troubleshooting

```bash
# Si tienes problemas con permisos en Linux
sudo chown -R $USER:$USER nombre_del_entorno

# Si el entorno virtual no se activa correctamente
python -m venv --clear nombre_del_entorno

# Verificar que pip está actualizado
python -m pip install --upgrade pip
```

## 📝 Mejores Prácticas

1. **Siempre usar entornos virtuales** para proyectos Python
2. **Incluir requirements.txt** en el control de versiones
3. **No incluir el directorio del entorno virtual** en git (usar .gitignore)
4. **Documentar la versión de Python** requerida
5. **Recrear el entorno** cuando cambies de máquina
6. **Usar nombres descriptivos** para los entornos virtuales

## 🚀 Configuración Inicial para este Proyecto

```bash
# 1. Clonar o descargar el proyecto
cd proyectoPythonMySQL

# 2. Crear entorno virtual
python3 -m venv mientorno  # Linux/Mac
python -m venv mientorno   # Windows

# 3. Activar entorno virtual
source mientorno/bin/activate  # Linux/Mac
mientorno\Scripts\activate     # Windows

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. ¡Listo para trabajar!
```

## 📚 Recursos Adicionales

- [Documentación oficial de venv](https://docs.python.org/3/library/venv.html)
- [Guía de pip](https://pip.pypa.io/en/stable/)
- [Mejores prácticas de Python](https://docs.python-guide.org/)

---

**¡Disfruta aprendiendo Python y la gestión de bases de datos!** 🎉
