# https://docs.streamlit.io/en/latest/caching.html キャッシュについて色々

import streamlit as st
import time

st.title('Caching')
'https://docs.streamlit.io/en/latest/caching.html'

st.subheader('Example 1: Basic usage')


@st.cache  # 👈 Added this
def expensive_computation(a, b):
    time.sleep(2)  # This makes the function take 2s to run
    return a * b


a = 2
b = 21
res = expensive_computation(a, b)
# 関数内の処理が変更されるとか引数が変更されない限りこの処理は再度行われることはない

st.write("Result:", res)


st.subheader('Example 4: When an inner function changes')
'別の関数までたどって変更を追ってくれるっぽい'


def inner_func(a, b):
    st.write("inner_func(", a, ",", b, ") ran")
    return a ** b


@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return inner_func(a, b) + 1


a = 2
b = 210
res = expensive_computation(a, b)

st.write("Result:", res)

st.subheader('Example 5: Use caching to speed up your app across users')

'一回計算した値は高速に返す'


@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b


a = 2
b = st.slider("Pick a number", 0, 10)  # 👈 Changed this
res = expensive_computation(a, b)

st.write("Result:", res)

st.subheader('Example 6: Mutating cached values')
@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return {"output": a * b}  # 👈 Mutable object


a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

# mutableなオブジェクトにあとから突っ込もうとすると警告が出るようになっている
res["output"] = "result was manually mutated"  # 👈 Mutated cached value

st.write("Mutated result:", res)
