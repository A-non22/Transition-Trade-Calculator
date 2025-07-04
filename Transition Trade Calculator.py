import streamlit as st

st.set_page_config(page_title="Transition Trade Calculator", layout="wide")

# Centered main heading
st.markdown(
    "<h1 style='text-align: center;'>Transition Trade Calculator</h1>",
    unsafe_allow_html=True
)

# Create two columns for the calculators
col1, col2 = st.columns(2)

# ------------------- Calculator 1: Trade Confidence -------------------
with col1:
    st.header("Trade Confidence")

    wdrr = st.selectbox("WDRR (Total credit -3)", options=[0, 1, 2, 3], key="wdrr")
    sequencing = st.selectbox("Sequencing Data (Total credit -3)", options=[0, 1, 2, 3], key="sequencing")
    ddr_target = st.selectbox("DDR Target hit (Total credit -3)", options=[0, 1, 2, 3], key="ddr_target")
    m7x_target = st.selectbox("M7X target hit (highest % and furthest) (Total credit -2)", options=[0, 1, 2], key="m7x_target")
    hard_rejection = st.selectbox("Hard Rejection (Total credit -1)", options=[0, 1], key="hard_rejection")
    structure_break = st.selectbox("Structure Break (Total credit -1)", options=[0, 1], key="structure_break")
    liquidity_trn = st.selectbox("Liquidity or TRN High/Low taken (Total credit -1)", options=[0, 1], key="liquidity_trn")

    # Total credit for Calculator 1 is fixed at 14
    base_total_credit_1 = 14
    obtained_credit_1 = (
        wdrr + sequencing + ddr_target + m7x_target +
        hard_rejection + structure_break + liquidity_trn
    )

    percentage_1 = (obtained_credit_1 / base_total_credit_1) * 100 if base_total_credit_1 > 0 else 0

    st.header("Results")
    st.markdown(
        f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_1} / {base_total_credit_1}</span></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3><b>Trade Confidence:</b> <span style='color:green;'>{percentage_1:.2f}%</span></h3>",
        unsafe_allow_html=True
    )


# ------------------- Updated Calculator 2: Entry Calculator -------------------
with col2:
    st.header("Entry Calculator")

    mdrc = st.selectbox("MDRC (Total credit -3)", options=[0, 1, 2, 3], key="mdrc")
    long_short = st.selectbox("Long/Short Structure (Total credit -2)", options=[0, 1, 2], key="long_short")
    svp_reject = st.selectbox("SVP Reject (Total credit -1)", options=[0, 1], key="svp_reject")
    bml_reject = st.selectbox("BML Reject (Total credit -1)", options=[0, 1], key="bml_reject")
    mb_reject = st.selectbox("MB Reject (Total credit -1)", options=[0, 1], key="mb_reject")
    db = st.selectbox("DB (Total credit -1)", options=[0, 1], key="db")
    wdrc_mid = st.selectbox("WDRC Mid (Total credit -1)", options=[0, 1], key="wdrc_mid")
    drc_reject = st.selectbox("DRC Reject (Total credit -1)", options=[0, 1], key="drc_reject")
    limiter_reject = st.selectbox("Limiter Reject (Total credit -1)", options=[0, 1], key="limiter_reject")
    drib_reject = st.selectbox("Drib Reject (Total credit -1)", options=[0, 1], key="drib_reject")
    m7box_reject = st.selectbox("M7Box Reject (Total credit -1)", options=[0, 1], key="m7box_reject")
    ddr_line_reject = st.selectbox("DDR Line Rejection (Total credit -1)", options=[0, 1], key="ddr_line_reject")
    wdrr_line_reject = st.selectbox("WDRR Line Rejection (Total credit -1)", options=[0, 1], key="wdrr_line_reject")
    half_reject = st.selectbox("0.5 Reject (Total credit -1)", options=[0, 1], key="half_reject")  # NEW INPUT

    obtained_credit_2 = (mdrc + long_short + svp_reject + bml_reject + mb_reject +
                         db + wdrc_mid + drc_reject + limiter_reject +
                         drib_reject + m7box_reject + ddr_line_reject + wdrr_line_reject + half_reject)

    total_possible_credit_2 = 17  # Updated total with new input

    percentage_2 = (obtained_credit_2 / total_possible_credit_2) * 100 if total_possible_credit_2 > 0 else 0

    st.header("Results")
    st.markdown(
        f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_2} / {total_possible_credit_2}</span></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3><b>Entry Quality:</b> <span style='color:green;'>{percentage_2:.2f}%</span></h3>",
        unsafe_allow_html=True
    )
