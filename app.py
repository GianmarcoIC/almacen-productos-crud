import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from database import init_db, Item

# Inicializar la base de datos
engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()

# Aplicar estilo CSS
st.markdown('<style>{}</style>'.format(open('style.css').read()), unsafe_allow_html=True)

# Título
st.title("Gestión de Almacén")

# Operaciones CRUD

# Crear un nuevo ítem
if st.button("Agregar Ítem"):
    nombre = st.text_input("Nombre del Ítem")
    cantidad = st.number_input("Cantidad", min_value=0, step=1)
    if st.button("Guardar"):
        nuevo_item = Item(nombre=nombre, cantidad=cantidad)
        session.add(nuevo_item)
        session.commit()
        st.success("Ítem agregado correctamente")

# Leer ítems
st.subheader("Lista de Ítems")
items = session.query(Item).all()
for item in items:
    st.write(f"ID: {item.id}, Nombre: {item.nombre}, Cantidad: {item.cantidad}")

# Actualizar un ítem
st.subheader("Actualizar Ítem")
id_actualizar = st.number_input("ID del Ítem a actualizar", min_value=1, step=1)
nuevo_nombre = st.text_input("Nuevo Nombre del Ítem")
nueva_cantidad = st.number_input("Nueva Cantidad", min_value=0, step=1)
if st.button("Actualizar"):
    item_a_actualizar = session.query(Item).filter_by(id=id_actualizar).first()
    if item_a_actualizar:
        item_a_actualizar.nombre = nuevo_nombre
        item_a_actualizar.cantidad = nueva_cantidad
        session.commit()
        st.success("Ítem actualizado correctamente")
    else:
        st.error("Ítem no encontrado")

# Eliminar un ítem
st.subheader("Eliminar Ítem")
id_eliminar = st.number_input("ID del Ítem a eliminar", min_value=1, step=1)
if st.button("Eliminar"):
    item_a_eliminar = session.query(Item).filter_by(id=id_eliminar).first()
    if item_a_eliminar:
        session.delete(item_a_eliminar)
        session.commit()
        st.success("Ítem eliminado correctamente")
    else:
        st.error("Ítem no encontrado")
