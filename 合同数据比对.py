import streamlit_antd_components as sac
import streamlit as st
import pandas as pd


def contractDiff():
    st.subheader(":red[多模态文件信息比对测试] > 合同数据 > 贷款业务")
    step_ph, btn_ph = st.empty(), st.empty()
    if 'steps' not in st.session_state:
        st.session_state['steps'] = "step 1"

    """操作区域"""
    with btn_ph.container():
        """第一步"""
        if st.session_state["steps"] == "step 1":
            for _ in range(3):
                st.write(" ")
            with st.container(height=400):
                for _ in range(2):
                    st.write(" ")
                sac.alert(label='⚠️**注意**',
                          description='目前「标准文件上传」仅支持单文件上传，且上传的原始数据文件仅支持.docx；「多模态文件上传」支持多个文件同时上传，支持.pdf/.docx/图片等格式',
                          size='sm', radius=20, color='dark', banner=[False, True])

                col1 = st.columns(2, gap='large')
                with col1[0]:
                    with st.form("文件上传"):
                        st.file_uploader("标准文件上传")
                        st.form_submit_button("⇲", disabled=True)

                with col1[1]:
                    with st.form("测试文件上传"):
                        st.file_uploader("多模态文件上传（支持上传多个文件）", accept_multiple_files=True)
                        st.form_submit_button("⇲", disabled=True, )

            col1_1 = st.columns(7)
            with col1_1[0]:
                sac.switch(label='忽略目录', size='md')
            with col1_1[1]:
                sac.switch(label='忽略页眉页脚', size='md', align='center')
            col1_ = st.columns(11)

            with col1_[10]:
                if st.button("下一步", key="btn1", type="primary"):
                    st.session_state["steps"] = "step 2"

        """第二步"""
        if st.session_state["steps"] == "step 2":
            st.session_state["steps"] = "step 2"
            with st.form("关键字选取"):
                st.subheader("关键字选取")
                sac.transfer(items=[f'item{i}' for i in range(30)], index=[0, 1],
                             titles=['source', 'target'],
                             reload=True, align='center', search=True, pagination=True)
                st.form_submit_button("⇲", disabled=True)
            col2 = st.columns(11)
            with col2[10]:
                if st.button("下一步", key="btn2", type="primary"):
                    st.session_state["steps"] = "step 3"
            with col2[9]:
                if st.button("上一步", key="btn2_", type="primary"):
                    st.session_state["steps"] = "step 1"

        """第三步"""
        if st.session_state["steps"] == "step 3":
            st.session_state["steps"] = "step 3"
            # 初始化数据
            if 'data' not in st.session_state:
                st.session_state.data = []

            # 创建两列布局
            col1, col2, col3 = st.columns([1, 2, 2])

            with col2:
                value = st.text_input('')
                # 显示当前数据

            with col3:
                for _ in range(2):
                    st.write(" ")

                if sac.buttons(
                        [sac.ButtonsItem(label='新增')], radius=20):

                    if value:  # 确保输入不为空
                        st.session_state.data.append(value)
            with col2:
                st.write("### 新增数据：")
                if st.session_state.data:
                    df = pd.DataFrame(st.session_state.data, columns=['新增数据'], index=None)
                    st.table(df)
            col3_ = st.columns(11)
            with col3_[9]:
                if st.button("下一步", key="btn3", type="primary"):
                    st.session_state["steps"] = "step 4"
        """第三步"""
        if st.session_state["steps"] == "step 4":
            st.session_state["steps"] = "step 4"
            col4 = st.columns([2, 2, 1])

            with col4[1]:
                st.write(":red[被测文件：]test合同.docx")
                st.write(":red[关键字：]item1、item2、item3")
            col4_ = st.columns(11)
            with col4_[9]:
                if st.button("开始测试", key="btn4", type="primary"):
                    pass

    """导航栏"""
    with step_ph.container():
        sac.steps(
            items=[
                sac.StepsItem(title='step 1', description='上传文件'),
                sac.StepsItem(title='step 2', description='选取抽取点'),
                sac.StepsItem(title='step 3', description='新增抽取点'),
                sac.StepsItem(title='step 4', description='确认信息'),
            ], key="steps", variant='navigation', format_func='title'
        )
