import streamlit as st
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos en un servidor en la nube (ejemplo)
# Reemplaza 'usuario', 'contraseña', 'host', 'puerto', y 'almacen_db' con tus datos reales
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

# Función principal para manejar la navegación y las operaciones CRUD
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

# Función para ver todos los productos
def ver_productos():
    st.subheader("Lista de Productos")
    query = select([productos])
    result = session.execute(query).fetchall()
    st.table(result)

# Función para agregar un nuevo producto
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

# Función para editar un producto existente
def editar_producto():
    st.subheader("Editar Producto")
    id_producto = st.number_input("ID del Producto a Editar", min_value=1, step=1)
    
    if id_producto:
        query = select([productos]).where(productos.c.id == id_producto)
        producto = session.execute(query).fetchone()
        
        if producto:
            nombre = st.text_input("Nombre del Producto", value=producto['nombre'])
            descripcion = st.text_area("Descripción", value=producto['descripcion'])
            precio = st.number_input("Precio", min_value=0.0, step=0.1, value=producto['precio'])
            cantidad = st.number_input("Cantidad", min_value=0, value=producto['cantidad'])

            if st.button("Actualizar Producto"):
                update = productos.update().where(productos.c.id == id_producto).values(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio,
                    cantidad=cantidad
                )
                session.execute(update)
                session.commit()
                st.success("Producto actualizado exitosamente")
        else:
            st.error("Producto no encontrado")

# Función para eliminar un producto
def eliminar_producto():
    st.subheader("Eliminar Producto")
    id_producto = st.number_input("ID del Producto a Eliminar", min_value=1, step=1)
    
    if st.button("Eliminar Producto"):
        delete = productos.delete().where(productos.c.id == id_producto)
        session.execute(delete)
        session.commit()
        st.success("Producto eliminado exitosamente")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
