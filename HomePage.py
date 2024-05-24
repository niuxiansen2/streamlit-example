import streamlit_antd_components as sac
import streamlit as st
from 合同数据比对 import *
from 调查报告 import *

st.set_page_config(page_title="业务审批运营要件工具", page_icon="📑", layout="wide")

with st.sidebar:
    st.image("logo.png", use_column_width=True)
    sac.menu([
        sac.MenuItem('主页', icon='house-fill', ),
        # sac.MenuItem('业务运营智能审批要件', icon='box-fill'),
        sac.MenuItem("👩🏻‍💻  多模态文件信息比对测试",  children=[
            sac.MenuItem('贷款业务'),
            # sac.MenuItem('调查报告'),
            # sac.MenuItem('授信批复'),
            # sac.MenuItem('申请表'),
            sac.MenuItem('更多类型文件'),
        ]),
        sac.MenuItem('🎭  合同版本智能比对', ),
        sac.MenuItem("📑  测试报告智能检核",),
        sac.MenuItem('🖥  UI智能核验', ),
        sac.MenuItem('🔖  更多功能', )]
        , key="menu", height=500, size=18, open_index=[1])
    for _ in range(20):
        st.write(" ")
    sac.switch(label='dark_modelight_mode', size='md', key="theme")

if st.session_state["menu"] == "贷款业务":
    contractDiff()

if st.session_state["menu"] == "调查报告":
    report()
