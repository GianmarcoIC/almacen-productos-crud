import streamlit as st
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos en un servidor en la nube (ejemplo)
engine = create_engine('mysql+pymysql://usuario:contraseña@host:puerto/almacen_db')
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

# Definición de la tabla productos
productos = Table(
    'productos', metadata,
    Column('id', Integer, primary_key=True),
    Column('nombre', String(100)),
    Column('descripcion', String(255)),
    Column('precio', Integer),
    Column('cantidad', Integer)
)

def main():
    st.title("Gestión de Almacén")
    st.sidebar.title("Operaciones CRUD")
    opcion = st.sidebar.selectbox("Seleccione una operación", ["Ver Productos", "Agregar Producto", "Editar Producto", "Eliminar Producto"])

    if opcion == "Ver Productos":
        ver_productos()
    elif opcion == "Agregar Producto":
        agregar_producto()
    elif opcion == "Editar Producto":
        editar_producto()
    elif opcion == "Eliminar Producto":
        eliminar_producto()

def ver_productos():
    st.subheader("Lista de Productos")
    query = select([productos])
    result = session.execute(query).fetchall()
    st.table(result)

def agregar_producto():
    st.subheader("Agregar Nuevo Producto")
    nombre = st.text_input("Nombre del Producto")
    descripcion = st.text_area("Descripción")
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    cantidad = st.number_input("Cantidad", min_value=0)

    if st.button("Agregar Producto"):
        ins = productos.insert().values(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad)
        session.execute(ins)
        session.commit()
        st.success("Producto agregado exitosamente")

def editar_producto():
    st.subheader("Editar Producto")
    # Aquí puedes implementar la edición

def eliminar_producto():
    st.subheader("Eliminar Producto")
    # Aquí puedes implementar la eliminación

if __name__ == "__main__":
    main()
