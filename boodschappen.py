import streamlit as st


def login():
    st.title("🔒 Login")
    password = st.text_input("Password", type="password", key="password")
    if st.button("Login"):
        if password == st.secrets.auth.password:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid password.")


def main_app():
    st.title("📝 Simple To-Do List")

    if "todos" not in st.session_state:
        st.session_state.todos = []

    new_task = st.text_input("Add a new task:")
    if st.button("Add"):
        if new_task:
            st.session_state.todos.append({"task": new_task, "done": False})

    for i, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.session_state.todos[i]["done"] = st.checkbox(
                todo["task"], value=todo["done"], key=i
            )
        with col2:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.todos.pop(i)
                st.experimental_rerun()

    if st.button("Clear Completed"):
        st.session_state.todos = [t for t in st.session_state.todos if not t["done"]]


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    main_app()
else:
    login()
