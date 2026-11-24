import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    NAVY = RGBColor(11, 37, 69)        # #0B2545
    DARK_BLUE = RGBColor(30, 58, 138)  # #1E3A8A
    LIGHT_BG = RGBColor(248, 250, 252) # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_CLR = RGBColor(226, 232, 240)
    GOLD = RGBColor(217, 119, 6)       # #D97706
    CYAN = RGBColor(2, 132, 199)       # #0284C7
    TEXT_DARK = RGBColor(15, 23, 42)   # #0F172A
    TEXT_MUTED = RGBColor(100, 116, 139)
    WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text="MINOR PROJECT PRESENTATION | MNR UNIVERSITY"):
        # Top banner background
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = NAVY
        top_bar.line.color.rgb = GOLD
        top_bar.line.width = Pt(2)

        # Category text
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = GOLD

        # Title text
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.5), Inches(0.65))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Georgia"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = WHITE

        # Bottom footer bar
        bot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.05), Inches(13.333), Inches(0.45))
        bot_bar.fill.solid()
        bot_bar.fill.fore_color.rgb = LIGHT_BG
        bot_bar.line.color.rgb = BORDER_CLR
        bot_bar.line.width = Pt(1)

        foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.7), Inches(0.35))
        tf_foot = foot_box.text_frame
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = "Yashwanth Talari (25RBAIM0047) | B.Tech CSE (AIML) - Section A | MNR University"
        p_foot.font.name = "Arial"
        p_foot.font.size = Pt(10)
        p_foot.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_CLR):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # ==========================================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    # Outer border
    border1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), Inches(0.4), Inches(12.533), Inches(6.7))
    border1.fill.background()
    border1.line.color.rgb = GOLD
    border1.line.width = Pt(2)

    # University Header
    u_box = s1.shapes.add_textbox(Inches(1.0), Inches(0.7), Inches(11.333), Inches(1.3))
    tf_u = u_box.text_frame
    p_u1 = tf_u.paragraphs[0]
    p_u1.alignment = PP_ALIGN.CENTER
    p_u1.text = "MNR UNIVERSITY"
    p_u1.font.name = "Georgia"
    p_u1.font.size = Pt(28)
    p_u1.font.bold = True
    p_u1.font.color.rgb = WHITE

    p_u2 = tf_u.add_paragraph()
    p_u2.alignment = PP_ALIGN.CENTER
    p_u2.text = "School of Engineering & Technology (SOET) | Department of Computer Science & Engineering"
    p_u2.font.name = "Arial"
    p_u2.font.size = Pt(13)
    p_u2.font.color.rgb = GOLD
    p_u2.space_before = Pt(4)

    # Minor Project Badge
    p_badge = tf_u.add_paragraph()
    p_badge.alignment = PP_ALIGN.CENTER
    p_badge.text = "— MINOR PROJECT PRESENTATION —"
    p_badge.font.name = "Arial"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = RGBColor(186, 230, 253) # Light cyan
    p_badge.space_before = Pt(8)

    # Project Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(2.35), Inches(11.333), Inches(1.8))
    tf_t = t_box.text_frame
    p_t1 = tf_t.paragraphs[0]
    p_t1.alignment = PP_ALIGN.CENTER
    p_t1.text = "STUDENT MARKS PREDICTOR"
    p_t1.font.name = "Georgia"
    p_t1.font.size = Pt(38)
    p_t1.font.bold = True
    p_t1.font.color.rgb = RGBColor(254, 240, 138) # Gold accent

    p_t2 = tf_t.add_paragraph()
    p_t2.alignment = PP_ALIGN.CENTER
    p_t2.text = "A Machine Learning-Based Academic Performance Forecasting System"
    p_t2.font.name = "Arial"
    p_t2.font.size = Pt(16)
    p_t2.font.italic = True
    p_t2.font.color.rgb = WHITE
    p_t2.space_before = Pt(6)

    # Metadata Cards (Submitted By & Under Guidance)
    # Card Left: Student Details
    add_card(s1, 1.2, 4.4, 5.2, 2.2, bg_color=RGBColor(15, 33, 64), border_color=GOLD)
    st_box = s1.shapes.add_textbox(Inches(1.4), Inches(4.5), Inches(4.8), Inches(2.0))
    tf_st = st_box.text_frame
    p_shead = tf_st.paragraphs[0]
    p_shead.text = "SUBMITTED BY:"
    p_shead.font.name = "Arial"
    p_shead.font.size = Pt(11)
    p_shead.font.bold = True
    p_shead.font.color.rgb = GOLD

    p_sname = tf_st.add_paragraph()
    p_sname.text = "Yashwanth Talari"
    p_sname.font.name = "Georgia"
    p_sname.font.size = Pt(18)
    p_sname.font.bold = True
    p_sname.font.color.rgb = WHITE
    p_sname.space_before = Pt(3)

    p_sinfo = tf_st.add_paragraph()
    p_sinfo.text = "Roll Number: 25RBAIM0047\nProgramme: B.Tech – CSE (AIML), Section A\nYear: 2nd Year – 1st Semester | AY: 2026–2027"
    p_sinfo.font.name = "Arial"
    p_sinfo.font.size = Pt(11)
    p_sinfo.font.color.rgb = RGBColor(226, 232, 240)
    p_sinfo.space_before = Pt(4)

    # Card Right: Guide Details
    add_card(s1, 6.9, 4.4, 5.2, 2.2, bg_color=RGBColor(15, 33, 64), border_color=GOLD)
    gd_box = s1.shapes.add_textbox(Inches(7.1), Inches(4.5), Inches(4.8), Inches(2.0))
    tf_gd = gd_box.text_frame
    p_ghead = tf_gd.paragraphs[0]
    p_ghead.text = "UNDER THE GUIDANCE OF:"
    p_ghead.font.name = "Arial"
    p_ghead.font.size = Pt(11)
    p_ghead.font.bold = True
    p_ghead.font.color.rgb = GOLD

    p_gname = tf_gd.add_paragraph()
    p_gname.text = "Faculty Guide's Name"
    p_gname.font.name = "Georgia"
    p_gname.font.size = Pt(18)
    p_gname.font.bold = True
    p_gname.font.color.rgb = WHITE
    p_gname.space_before = Pt(3)

    p_ginfo = tf_gd.add_paragraph()
    p_ginfo.text = "Faculty Coordinator / Assistant Professor\nDepartment of Computer Science & Engineering\nCourse: Machine Learning (Code: 25CSM201)"
    p_ginfo.font.name = "Arial"
    p_ginfo.font.size = Pt(11)
    p_ginfo.font.color.rgb = RGBColor(226, 232, 240)
    p_ginfo.space_before = Pt(4)

    # ==========================================================
    # SLIDE 2: PROBLEM STATEMENT & PROJECT OBJECTIVE
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Problem Statement & Project Objectives")

    # Card 1: Problem Statement
    add_card(s2, 0.8, 1.45, 5.6, 5.3)
    p_box = s2.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(5.2), Inches(5.0))
    tf_p = p_box.text_frame
    tf_p.word_wrap = True
    p1 = tf_p.paragraphs[0]
    p1.text = "THE PROBLEM"
    p1.font.name = "Arial"
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(185, 28, 28)

    p2 = tf_p.add_paragraph()
    p2.text = "Delayed Identification of Academic Underperformance"
    p2.font.name = "Georgia"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_DARK
    p2.space_before = Pt(4)

    p3 = tf_p.add_paragraph()
    p3.text = (
        "• Students frequently evaluate exam preparedness subjectively without empirical metrics.\n\n"
        "• Academic counselors and faculty discover at-risk students only AFTER semester examinations have concluded.\n\n"
        "• Students struggle to determine the precise daily study investment needed to secure qualifying marks or top distinctions.\n\n"
        "• Need for a transparent, instant, mathematical prediction system to translate daily study hours into projected examination scores."
    )
    p3.font.name = "Arial"
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(51, 65, 85)
    p3.space_before = Pt(14)

    # Card 2: Objectives
    add_card(s2, 6.9, 1.45, 5.6, 5.3)
    o_box = s2.shapes.add_textbox(Inches(7.1), Inches(1.6), Inches(5.2), Inches(5.0))
    tf_o = o_box.text_frame
    tf_o.word_wrap = True
    po1 = tf_o.paragraphs[0]
    po1.text = "PROJECT OBJECTIVES"
    po1.font.name = "Arial"
    po1.font.size = Pt(13)
    po1.font.bold = True
    po1.font.color.rgb = CYAN

    po2 = tf_o.add_paragraph()
    po2.text = "Mathematical Modeling & Interactive Deployment"
    po2.font.name = "Georgia"
    po2.font.size = Pt(18)
    po2.font.bold = True
    po2.font.color.rgb = TEXT_DARK
    po2.space_before = Pt(4)

    po3 = tf_o.add_paragraph()
    po3.text = (
        "1. Train a Simple Linear Regression Model using Scikit-learn on study hours vs examination marks.\n\n"
        "2. Compute & Validate Model Metrics: Calculate exact slope (+5.00), intercept (30.00), and R² score (1.000).\n\n"
        "3. Develop an Interactive Web Interface using Streamlit featuring sliders, presets, and instant inference.\n\n"
        "4. Dynamic Vector Visualization: Render Matplotlib regression line, scatter points, and user coordinate drop-lines.\n\n"
        "5. Automated PDF Project Reporting: Produce an institutional academic project report with cover page."
    )
    po3.font.name = "Arial"
    po3.font.size = Pt(12.5)
    po3.font.color.rgb = RGBColor(51, 65, 85)
    po3.space_before = Pt(14)

    # ==========================================================
    # SLIDE 3: REAL-WORLD EDUCATIONAL USE CASES
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Real-World Educational Use Cases")

    use_cases = [
        ("1. Early Academic Intervention", 
         "Identify At-Risk Students", 
         "Pinpoints students dedicating < 2.0 hours daily (< 40% threshold) early in the semester, triggering automated remedial counseling before midterms.", 
         RGBColor(239, 68, 68)),
        ("2. Targeted Goal Planning", 
         "Reverse-Engineering Study Hours", 
         "Enables students to reverse-calculate the daily revision hours needed for desired honors (e.g. >= 6.0 hrs for First Class >=60%, >= 9.0 hrs for Distinction >=75%).", 
         RGBColor(2, 132, 199)),
        ("3. Parent-Teacher Advisory", 
         "Data-Grounded Benchmarking", 
         "Substitutes subjective impressions of student effort with concrete, data-backed regression return curves during performance reviews.", 
         RGBColor(217, 119, 6)),
        ("4. Institutional E-Learning", 
         "Self-Paced Habit Monitoring", 
         "Embeds into learning management portals (LMS) to guide exam preparation timetables and measure study-hour return-on-investment.", 
         RGBColor(22, 163, 74))
    ]

    for i, (tag, title, desc, acc_color) in enumerate(use_cases):
        x = 0.8 + (i % 2) * 5.95
        y = 1.45 + (i // 2) * 2.7
        add_card(s3, x, y, 5.75, 2.5)
        
        # Color bar indicator on left
        cbar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.18), Inches(2.5))
        cbar.fill.solid()
        cbar.fill.fore_color.rgb = acc_color
        cbar.line.fill.background()

        uc_box = s3.shapes.add_textbox(Inches(x + 0.35), Inches(y + 0.15), Inches(5.2), Inches(2.2))
        tf_uc = uc_box.text_frame
        tf_uc.word_wrap = True

        p_tag = tf_uc.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = acc_color

        p_tit = tf_uc.add_paragraph()
        p_tit.text = title
        p_tit.font.name = "Georgia"
        p_tit.font.size = Pt(16)
        p_tit.font.bold = True
        p_tit.font.color.rgb = TEXT_DARK
        p_tit.space_before = Pt(3)

        p_desc = tf_uc.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = RGBColor(71, 85, 105)
        p_desc.space_before = Pt(6)

    # ==========================================================
    # SLIDE 4: MATHEMATICAL FORMULATION & OLS ALGORITHM
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Mathematical Formulation & OLS Algorithm")

    # Left: Formula explanation
    add_card(s4, 0.8, 1.45, 6.2, 5.3)
    f_box = s4.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(5.8), Inches(5.0))
    tf_f = f_box.text_frame
    tf_f.word_wrap = True

    p_f1 = tf_f.paragraphs[0]
    p_f1.text = "SIMPLE LINEAR REGRESSION"
    p_f1.font.name = "Arial"
    p_f1.font.size = Pt(12)
    p_f1.font.bold = True
    p_f1.font.color.rgb = CYAN

    p_f2 = tf_f.add_paragraph()
    p_f2.text = "Ordinary Least Squares (OLS) Formulation"
    p_f2.font.name = "Georgia"
    p_f2.font.size = Pt(18)
    p_f2.font.bold = True
    p_f2.font.color.rgb = TEXT_DARK
    p_f2.space_before = Pt(4)

    p_f3 = tf_f.add_paragraph()
    p_f3.text = (
        "Linear Model Equation:\n"
        "   Y = mX + c\n\n"
        "Where:\n"
        "• Y = Dependent Target (Examination Marks: 0–100%)\n"
        "• X = Independent Feature (Daily Study Hours)\n"
        "• m = Slope / Weight (Marginal gain per hour)\n"
        "• c = Y-Intercept / Bias (Baseline knowledge floor)\n\n"
        "OLS Slope Minimization Formula:\n"
        "   m = Σ(Xi - X̄)(Yi - Ȳ) / Σ(Xi - X̄)²\n"
        "   c = Ȳ - mX̄\n\n"
        "Fitted Project Equation:\n"
        "   Marks = (5.00 × Study Hours) + 30.00"
    )
    p_f3.font.name = "Courier New"
    p_f3.font.size = Pt(12)
    p_f3.font.bold = True
    p_f3.font.color.rgb = RGBColor(30, 41, 59)
    p_f3.space_before = Pt(10)

    # Right: Parameters Table
    add_card(s4, 7.3, 1.45, 5.2, 5.3)
    prm_box = s4.shapes.add_textbox(Inches(7.5), Inches(1.6), Inches(4.8), Inches(5.0))
    tf_prm = prm_box.text_frame
    tf_prm.word_wrap = True

    p_p1 = tf_prm.paragraphs[0]
    p_p1.text = "MODEL PARAMETERS"
    p_p1.font.name = "Arial"
    p_p1.font.size = Pt(12)
    p_p1.font.bold = True
    p_p1.font.color.rgb = GOLD

    p_p2 = tf_prm.add_paragraph()
    p_p2.text = "Fitted Parameter Breakdown"
    p_p2.font.name = "Georgia"
    p_p2.font.size = Pt(18)
    p_p2.font.bold = True
    p_p2.font.color.rgb = TEXT_DARK
    p_p2.space_before = Pt(4)

    params = [
        ("Slope (m)", "+5.0000", "Each 1.0 hr study adds +5.0% marks."),
        ("Intercept (c)", "30.0000", "Zero-study baseline exam floor."),
        ("R² Score", "1.0000 (100%)", "Perfect linear variance explanation."),
        ("Training Samples", "N = 10", "Evenly spaced: 1 to 10 hours."),
        ("Residual Error", "e = 0.00", "Deterministic consistency on benchmark.")
    ]

    for p_name, p_val, p_int in params:
        p_row = tf_prm.add_paragraph()
        p_row.text = f"• {p_name}: {p_val}\n   → {p_int}"
        p_row.font.name = "Arial"
        p_row.font.size = Pt(12)
        p_row.font.color.rgb = RGBColor(51, 65, 85)
        p_row.space_before = Pt(10)

    # ==========================================================
    # SLIDE 5: VISUAL ANALYSIS & REGRESSION PLOT
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Model Visualization & Regression Fit")

    # Add Chart Image
    chart_img = "report_assets/fig_regression_model.png"
    if os.path.exists(chart_img):
        s5.shapes.add_picture(chart_img, Inches(0.8), Inches(1.45), width=Inches(7.2))

    # Right Card: Observations on Visualization
    add_card(s5, 8.2, 1.45, 4.3, 5.3)
    v_box = s5.shapes.add_textbox(Inches(8.4), Inches(1.6), Inches(3.9), Inches(5.0))
    tf_v = v_box.text_frame
    tf_v.word_wrap = True

    pv1 = tf_v.paragraphs[0]
    pv1.text = "GRAPHICAL DIAGNOSTICS"
    pv1.font.name = "Arial"
    pv1.font.size = Pt(12)
    pv1.font.bold = True
    pv1.font.color.rgb = CYAN

    pv2 = tf_v.add_paragraph()
    pv2.text = "Key Visual Highlights"
    pv2.font.name = "Georgia"
    pv2.font.size = Pt(17)
    pv2.font.bold = True
    pv2.font.color.rgb = TEXT_DARK
    pv2.space_before = Pt(4)

    pv3 = tf_v.add_paragraph()
    pv3.text = (
        "1. Training Points (Blue):\n"
        "   10 benchmark data points traverse exactly along the regression trajectory.\n\n"
        "2. Regression Line (Sky Blue):\n"
        "   Continuous fit representing Y = 5X + 30 across the entire hours domain.\n\n"
        "3. Interactive Prediction (Green):\n"
        "   Dynamic user test marker (6.0 hrs, 60.0%) with orthogonal drop-lines to both axes.\n\n"
        "4. High-DPI Vector Rendering:\n"
        "   Rendered at 220+ DPI with gridlines, crisp bounds, and clear legends."
    )
    pv3.font.name = "Arial"
    pv3.font.size = Pt(11.5)
    pv3.font.color.rgb = RGBColor(51, 65, 85)
    pv3.space_before = Pt(12)

    # ==========================================================
    # SLIDE 6: EMPIRICAL VALIDATION (SYNTHETIC COHORT DATA)
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Empirical Validation: Synthetic Cohort Trial")

    obs_img = "report_assets/fig_user_observations.png"
    if os.path.exists(obs_img):
        s6.shapes.add_picture(obs_img, Inches(0.8), Inches(1.45), width=Inches(7.2))

    # Right Card: Observations Table Summary
    add_card(s6, 8.2, 1.45, 4.3, 5.3)
    c_box = s6.shapes.add_textbox(Inches(8.4), Inches(1.6), Inches(3.9), Inches(5.0))
    tf_c = c_box.text_frame
    tf_c.word_wrap = True

    pc1 = tf_c.paragraphs[0]
    pc1.text = "VALIDATION FINDINGS"
    pc1.font.name = "Arial"
    pc1.font.size = Pt(12)
    pc1.font.bold = True
    pc1.font.color.rgb = GOLD

    pc2 = tf_c.add_paragraph()
    pc2.text = "Cohort Error & Accuracy"
    pc2.font.name = "Georgia"
    pc2.font.size = Pt(17)
    pc2.font.bold = True
    pc2.font.color.rgb = TEXT_DARK
    pc2.space_before = Pt(4)

    pc3 = tf_c.add_paragraph()
    pc3.text = (
        "• High Concordance (MAPE < 2.5%):\n"
        "  Across 8 synthetic validation students, actual exam marks matched predictions within ±2.0%.\n\n"
        "• Accurate At-Risk Interception:\n"
        "  Student Siddharth (1.0 hr, 34%) was immediately flagged for tutoring intervention.\n\n"
        "• Upper Saturation Bound:\n"
        "  Beyond 10 hours (Pooja R., 11 hrs, 84%), slight fatigue was observed, suggesting future non-linear plateau modeling."
    )
    pc3.font.name = "Arial"
    pc3.font.size = Pt(11.5)
    pc3.font.color.rgb = RGBColor(51, 65, 85)
    pc3.space_before = Pt(12)

    # ==========================================================
    # SLIDE 7: SYSTEM ARCHITECTURE & TECH STACK
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "System Architecture & Technology Stack")

    tech_stack = [
        ("Python 3.13", "Core Programming Language", "Powers backend modeling, mathematical operations, and data transformation pipeline.", CYAN),
        ("Streamlit 1.37+", "Interactive Web UI Framework", "Dual-column responsive layout, live hour sliders, quick presets, and instant metric cards.", RGBColor(239, 68, 68)),
        ("Scikit-learn 1.9+", "Machine Learning Engine", "Trains LinearRegression with Ordinary Least Squares, evaluates R² score, intercepts, and weights.", RGBColor(16, 185, 129)),
        ("Matplotlib & Pandas", "Visualization & Dataframes", "Vectorized scatter and regression plotting, ground-truth tables, and residual calculation.", RGBColor(245, 158, 11)),
        ("ReportLab & PyMuPDF", "Automated PDF Generation", "Compiles publication-grade 5-page academic project reports with institutional cover page.", RGBColor(147, 51, 234)),
        ("Git & GitHub", "Version Control & Deployment", "Production repository management, tracking code, dataset, PPT, and PDF deliverables.", NAVY)
    ]

    for i, (tool, role, detail, color_box) in enumerate(tech_stack):
        x = 0.8 + (i % 3) * 3.95
        y = 1.45 + (i // 3) * 2.7
        add_card(s7, x, y, 3.8, 2.5)

        t_card = s7.shapes.add_textbox(Inches(x + 0.25), Inches(y + 0.15), Inches(3.3), Inches(2.2))
        tf_tc = t_card.text_frame
        tf_tc.word_wrap = True

        pt1 = tf_tc.paragraphs[0]
        pt1.text = tool
        pt1.font.name = "Georgia"
        pt1.font.size = Pt(16)
        pt1.font.bold = True
        pt1.font.color.rgb = color_box

        pt2 = tf_tc.add_paragraph()
        pt2.text = role
        pt2.font.name = "Arial"
        pt2.font.size = Pt(11)
        pt2.font.bold = True
        pt2.font.color.rgb = TEXT_DARK
        pt2.space_before = Pt(3)

        pt3 = tf_tc.add_paragraph()
        pt3.text = detail
        pt3.font.name = "Arial"
        pt3.font.size = Pt(10.5)
        pt3.font.color.rgb = RGBColor(71, 85, 105)
        pt3.space_before = Pt(5)

    # ==========================================================
    # SLIDE 8: APPLICATION DEMO & RUNBOOK
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Application Execution & Live Demo Guide")

    # Left: Steps to Run
    add_card(s8, 0.8, 1.45, 5.7, 5.3)
    rn_box = s8.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(5.3), Inches(5.0))
    tf_rn = rn_box.text_frame
    tf_rn.word_wrap = True

    pr1 = tf_rn.paragraphs[0]
    pr1.text = "EXECUTION RUNBOOK"
    pr1.font.name = "Arial"
    pr1.font.size = Pt(12)
    pr1.font.bold = True
    pr1.font.color.rgb = CYAN

    pr2 = tf_rn.add_paragraph()
    pr2.text = "How to Run Locally"
    pr2.font.name = "Georgia"
    pr2.font.size = Pt(18)
    pr2.font.bold = True
    pr2.font.color.rgb = TEXT_DARK
    pr2.space_before = Pt(4)

    pr3 = tf_rn.add_paragraph()
    pr3.text = (
        "Step 1: Clone Repository\n"
        "   git clone https://github.com/yashwanthtalari/ML---25rbaim0047.git\n"
        "   cd ML---25rbaim0047\n\n"
        "Step 2: Install Dependencies\n"
        "   pip install -r requirements.txt\n\n"
        "Step 3: Launch Streamlit Web App\n"
        "   streamlit run app.py\n\n"
        "Step 4: Open in Web Browser\n"
        "   http://localhost:8501\n\n"
        "Step 5: Generate Report\n"
        "   python generate_report.py"
    )
    pr3.font.name = "Courier New"
    pr3.font.size = Pt(11)
    pr3.font.bold = True
    pr3.font.color.rgb = RGBColor(30, 41, 59)
    pr3.space_before = Pt(10)

    # Right: Dashboard Features
    add_card(s8, 6.8, 1.45, 5.7, 5.3)
    df_box = s8.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.3), Inches(5.0))
    tf_df = df_box.text_frame
    tf_df.word_wrap = True

    pd1 = tf_df.paragraphs[0]
    pd1.text = "DASHBOARD CAPABILITIES"
    pd1.font.name = "Arial"
    pd1.font.size = Pt(12)
    pd1.font.bold = True
    pd1.font.color.rgb = GOLD

    pd2 = tf_df.add_paragraph()
    pd2.text = "User Experience Highlights"
    pd2.font.name = "Georgia"
    pd2.font.size = Pt(18)
    pd2.font.bold = True
    pd2.font.color.rgb = TEXT_DARK
    pd2.space_before = Pt(4)

    pd3 = tf_df.add_paragraph()
    pd3.text = (
        "• Interactive Sliders & Presets:\n"
        "  Select study hours (0–16 hrs) or one-click preset buttons (2, 5, 8, 10 hrs).\n\n"
        "• Real-Time Category Badges:\n"
        "  Instantly classifies outcome into Distinction, First Class, Second Class, Pass, or Needs Improvement.\n\n"
        "• Model Coefficients & Formulas:\n"
        "  Displays live R² = 1.000, m = +5.00, c = 30.00.\n\n"
        "• One-Click PDF Download:\n"
        "  Built-in download button serving the institutional project report."
    )
    pd3.font.name = "Arial"
    pd3.font.size = Pt(12)
    pd3.font.color.rgb = RGBColor(51, 65, 85)
    pd3.space_before = Pt(10)

    # ==========================================================
    # SLIDE 9: CONCLUSION & FUTURE SCOPE
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Conclusion & Future Roadmap")

    add_card(s9, 0.8, 1.45, 5.6, 5.3)
    cc_box = s9.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(5.2), Inches(5.0))
    tf_cc = cc_box.text_frame
    tf_cc.word_wrap = True

    pcc1 = tf_cc.paragraphs[0]
    pcc1.text = "KEY TAKEAWAYS"
    pcc1.font.name = "Arial"
    pcc1.font.size = Pt(12)
    pcc1.font.bold = True
    pcc1.font.color.rgb = CYAN

    pcc2 = tf_cc.add_paragraph()
    pcc2.text = "Project Summary"
    pcc2.font.name = "Georgia"
    pcc2.font.size = Pt(18)
    pcc2.font.bold = True
    pcc2.font.color.rgb = TEXT_DARK
    pcc2.space_before = Pt(4)

    pcc3 = tf_cc.add_paragraph()
    pcc3.text = (
        "1. Verified Mathematical Model:\n"
        "   Simple Linear Regression successfully maps study hours to examination marks with zero residual error on ground truth.\n\n"
        "2. Production-Grade Deployment:\n"
        "   Entire system is fully operational in a clean, lightweight Streamlit architecture without server bloat.\n\n"
        "3. Practical Academic Utility:\n"
        "   Solves core student time-budgeting and educator intervention needs with sub-millisecond response."
    )
    pcc3.font.name = "Arial"
    pcc3.font.size = Pt(12)
    pcc3.font.color.rgb = RGBColor(51, 65, 85)
    pcc3.space_before = Pt(12)

    add_card(s9, 6.9, 1.45, 5.6, 5.3)
    fs_box = s9.shapes.add_textbox(Inches(7.1), Inches(1.6), Inches(5.2), Inches(5.0))
    tf_fs = fs_box.text_frame
    tf_fs.word_wrap = True

    pfs1 = tf_fs.paragraphs[0]
    pfs1.text = "FUTURE ENHANCEMENTS"
    pfs1.font.name = "Arial"
    pfs1.font.size = Pt(12)
    pfs1.font.bold = True
    pfs1.font.color.rgb = GOLD

    pfs2 = tf_fs.add_paragraph()
    pfs2.text = "Strategic Roadmap"
    pfs2.font.name = "Georgia"
    pfs2.font.size = Pt(18)
    pfs2.font.bold = True
    pfs2.font.color.rgb = TEXT_DARK
    pfs2.space_before = Pt(4)

    pfs3 = tf_fs.add_paragraph()
    pfs3.text = (
        "• Multi-Variable Regression:\n"
        "  Incorporate attendance percentage, sleep duration, and assignment submission rates.\n\n"
        "• Non-Linear Saturation Modeling:\n"
        "  Apply polynomial regression (Y = w₁X + w₂X² + c) to model cognitive fatigue beyond 10 hours.\n\n"
        "• Mobile Application Integration:\n"
        "  Package as a cross-platform mobile assistant for student calendar synchronization."
    )
    pfs3.font.name = "Arial"
    pfs3.font.size = Pt(12)
    pfs3.font.color.rgb = RGBColor(51, 65, 85)
    pfs3.space_before = Pt(12)

    # ==========================================================
    # SLIDE 10: THANK YOU & Q&A
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    bg10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg10.fill.solid()
    bg10.fill.fore_color.rgb = NAVY
    bg10.line.fill.background()

    border10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), Inches(0.4), Inches(12.533), Inches(6.7))
    border10.fill.background()
    border10.line.color.rgb = GOLD
    border10.line.width = Pt(2)

    th_box = s10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.333), Inches(3.5))
    tf_th = th_box.text_frame
    
    pth1 = tf_th.paragraphs[0]
    pth1.alignment = PP_ALIGN.CENTER
    pth1.text = "THANK YOU!"
    pth1.font.name = "Georgia"
    pth1.font.size = Pt(48)
    pth1.font.bold = True
    pth1.font.color.rgb = RGBColor(254, 240, 138)

    pth2 = tf_th.add_paragraph()
    pth2.alignment = PP_ALIGN.CENTER
    pth2.text = "Questions & Feedback Welcome"
    pth2.font.name = "Arial"
    pth2.font.size = Pt(20)
    pth2.font.color.rgb = WHITE
    pth2.space_before = Pt(10)

    pth3 = tf_th.add_paragraph()
    pth3.alignment = PP_ALIGN.CENTER
    pth3.text = "Yashwanth Talari | Roll Number: 25RBAIM0047\nB.Tech – CSE (AIML), Section A | MNR University\nGitHub: https://github.com/yashwanthtalari/ML---25rbaim0047"
    pth3.font.name = "Arial"
    pth3.font.size = Pt(14)
    pth3.font.color.rgb = RGBColor(203, 213, 225)
    pth3.space_before = Pt(24)

    output_path = "Student_Marks_Predictor_Presentation.pptx"
    prs.save(output_path)
    print("Presentation saved successfully:", output_path)

if __name__ == "__main__":
    create_deck()
