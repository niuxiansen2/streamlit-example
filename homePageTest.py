import streamlit_antd_components as sac
import streamlit as st

st.set_page_config(page_title="业务审批运营要件工具", page_icon="📑", layout="wide")

with st.sidebar:
    sac.menu([
        sac.MenuItem('主页', icon='house-fill', ),
        # sac.MenuItem('业务运营智能审批要件', icon='box-fill'),
        sac.MenuItem("多模态文件信息比对测试", icon='apple', children=[
            sac.MenuItem('合同数据'),
            sac.MenuItem('调查报告'),
            sac.MenuItem('授信批复'),
            sac.MenuItem('申请表'),
            sac.MenuItem('更多类型文件'),
        ]),
        sac.MenuItem('合同版本智能比对', icon='git', description='other items'),
        sac.MenuItem("测试报告智能检核", icon='google', description='item description'),
        sac.MenuItem('UI智能核验', icon='gitlab'),
        sac.MenuItem('wechat', icon='wechat')]
        , key="menu", height=500, size=18, open_index=[1])

    st.file_uploader("test")

if st.session_state["menu"] == "合同数据":

    st.subheader("多模态文件信息比对测试 > 合同数据")
    sac.steps(
        items=[
            sac.StepsItem(title='step 1', description='上传文件'),
            sac.StepsItem(title='step 2', description='参数选择'),
            sac.StepsItem(title='step 3', description='数据预处理'),
            sac.StepsItem(title='step 4', description='模型预测'),
        ], key="steps", variant='navigation',
    )
    if st.session_state["steps"] == "step 1":
        st.session_state["steps"] = "step 2"
        st.subheader("step 1")
        st.write("step 1")
        if st.button("下一步"):
            st.session_state["steps"] = "step 2"

            sac.transfer(items=[f'item{i}' for i in range(30)], label='关键字选择', index=[0, 1],
                         titles=['source', 'target'],
                         reload=True, align='center', search=True, pagination=True)
