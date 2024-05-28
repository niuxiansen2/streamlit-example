import time

import streamlit_antd_components as sac
import pandas as pd
from contractDiffReport import *


@st.experimental_dialog("文本解析")
def docProcess():
    st.subheader(":red[多模态文件信息提取]")
    progress_text = "文本解析中..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)


def contractDiff():
    st.subheader("👩🏻‍💻  :red[多模态文件信息比对测试] > 贷款业务")
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
                        st.file_uploader("多模态文件上传（支持上传多个文件）", accept_multiple_files=True,
                                         key="file_uploader2")

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

                sac.transfer(
                    items=["甲方姓名", "甲方证件号码", "甲方联系方式", "乙方姓名", "乙方证件号码", "乙方联系方式",
                           "贷款金额",
                           "货款用途",
                           "贷款支付对象", "贷款利率确定方式定价基础利率",
                           "期限档次",
                           "调整方式",
                           "利率调整日",
                           "调鍪周期",
                           "提前还款",
                           "贴息",
                           "抵押物保险",
                           "抵押登记",
                           "个人抵押房产清单",
                           "房屋坐落",
                           "房屋产权人"],
                    titles=['待选数据', '已选择数据'],
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
        """第四步"""
        if st.session_state["steps"] == "step 4":
            st.session_state["steps"] = "step 4"
            col4_ = st.columns([3, 8])

            with col4_[0]:
                with st.container(height=900):
                    st.subheader("结果列表", divider="red")
                    sac.tree(items=[
                        sac.TreeItem('📂抵押合同', description='/Users/nwj/Desktop/抵押合同.docx', children=[
                            sac.TreeItem('item2-2-1', tag=sac.Tag('未通过', color='red', size='sm'), ),
                            sac.TreeItem('item2-2-2', tag=sac.Tag('通过', color='cyan')),
                            sac.TreeItem('item2-2-3', tag=sac.Tag('通过', color='cyan')),
                            sac.TreeItem('item3-1', tag=sac.Tag('通过', color='cyan')),
                            sac.TreeItem('item3-2', tag=sac.Tag('通过', color='cyan')),
                            sac.TreeItem('item3-1', tag=sac.Tag('通过', color='cyan')),
                            sac.TreeItem('item3-2', tag=sac.Tag('通过', color='cyan')),
                        ], tag=[sac.Tag('通过', color='cyan')]),

                        sac.TreeItem('📂房抵经营_共借_电子调查报告', icon='',
                                     description='/Users/nwj/Desktop/房抵经营_共借_电子调查报告.pdf', children=[
                                sac.TreeItem('产品名称', tag=sac.Tag('通过', color='red', size='sm'), ),
                                sac.TreeItem('甲方姓名', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('额度金额（元）', tag=sac.Tag('未通过', color='red')),
                                sac.TreeItem('消费额度（元）', tag=sac.Tag('未通过', color='red')),
                                sac.TreeItem('额度期限（月）', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('经办机构', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('共借人姓名', tag=sac.Tag('未通过', color='red')),
                            ]),
                        sac.TreeItem('📂抵经营_共借_批复文件',
                                     description='/Users/nwj/Desktop/房抵经营_共借_电子调查报告.pdf', children=[
                                sac.TreeItem('item2-2-1', tag=sac.Tag('未通过', color='red', size='sm'), ),
                                sac.TreeItem('item2-2-2', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('item2-2-3', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('item3-1', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('item3-2', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('item3-1', tag=sac.Tag('通过', color='cyan')),
                                sac.TreeItem('item3-2', tag=sac.Tag('通过', color='cyan')),
                            ]),
                    ], index=0, size='lg', open_all=True)

            with col4_[1]:
                for _ in range(1):
                    st.write(" ")
                st.subheader("错误详情")
                with st.form("错误详情"):
                    # 创建数据
                    data = {
                        '数据名称': ['额度金额'],
                        '原始数据': ['2000000.00'],
                        '错误数据': ['3000000.00']
                    }

                    # 使用 pandas 创建 DataFrame
                    df = pd.DataFrame(data)

                    # 显示表格
                    st.dataframe(df, hide_index=True)  # 或者使用 st.table(df) 显示静态表格

                    with st.container(height=500):
                        st.image("img/report.png")

                    st.form_submit_button("保存结果")

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
