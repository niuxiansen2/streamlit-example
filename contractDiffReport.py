import streamlit as st
import json

# 示例测试报告数据
report_data = {
    "Test Suite 1": {
        "status": "passed",
        "steps": {
            "Step 1": {
                "status": "passed",
                "details": "Step 1 executed successfully."
            },
            "Step 2": {
                "status": "failed",
                "details": "Step 2 encountered an error."
            },
            "Step 3": {
                "status": "passed",
                "details": "Step 3 executed successfully."
            }
        }
    },
    "Test Suite 2": {
        "status": "failed",
        "steps": {
            "Step 1": {
                "status": "passed",
                "details": "Step 1 executed successfully."
            },
            "Step 2": {
                "status": "passed",
                "details": "Step 2 executed successfully."
            },
            "Step 3": {
                "status": "failed",
                "details": "Step 3 encountered an error."
            }
        }
    }
}


def report_display():
    # 设置页面标题
    st.title('结果比对报告')
    st.markdown(':gray[✅ --表示测试成功，❌ --表示测试失败]')
    # 初始化session state用于存储选中的步骤
    if 'selected_step' not in st.session_state:
        st.session_state.selected_step = None

    # 使用列布局
    left_column, right_column = st.columns([2, 3])

    with left_column:
        st.header('原始数据列表')

        def display_steps(steps, suite_name, level=0):
            for step, data in steps.items():
                status = data['status']
                icon = '✅' if status == 'passed' else '❌'
                step_name = f"{suite_name} - {step}"
                if st.button(f"{icon} {step}", key=step_name):
                    st.session_state.selected_step = step_name

        # 展示树形结构
        for suite, data in report_data.items():
            st.markdown(f"**{suite}**")
            display_steps(data['steps'], suite, level=1)

    with right_column:
        st.header('步骤详情')

        if st.session_state.selected_step:
            suite, step = st.session_state.selected_step.split(' - ')
            details = report_data[suite]['steps'][step]['details']
            st.markdown(f"{step}")
            st.markdown(details)
        else:
            st.write("请选择一个步骤查看详情。")
