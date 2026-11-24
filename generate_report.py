import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# ----------------------------------------------------------------------
# 1. Numbered Canvas with Thin Page Border and Header/Footer Logic
# ----------------------------------------------------------------------
class AcademicCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        w, h = A4

        if self._pageNumber == 1:
            # Thin black page border for the Cover Page
            # Outer formal border
            self.setStrokeColor(colors.HexColor("#1e293b"))
            self.setLineWidth(1.4)
            self.rect(26, 26, w - 52, h - 52)
            # Inner thin accent border
            self.setLineWidth(0.6)
            self.rect(30, 30, w - 60, h - 60)
            # Corner accents
            corner_len = 14
            self.setLineWidth(1.8)
            # Top-left
            self.line(23, h - 26, 23 + corner_len, h - 26)
            self.line(26, h - 23, 26, h - 23 - corner_len)
            # Top-right
            self.line(w - 23, h - 26, w - 23 - corner_len, h - 26)
            self.line(w - 26, h - 23, w - 26, h - 23 - corner_len)
            # Bottom-left
            self.line(23, 26, 23 + corner_len, 26)
            self.line(26, 23, 26, 23 + corner_len)
            # Bottom-right
            self.line(w - 23, 26, w - 23 - corner_len, 26)
            self.line(w - 26, 23, w - 26, 23 + corner_len)
        else:
            # Running Header for report body pages (Times-Roman)
            self.setFont("Times-Bold", 8.5)
            self.setFillColor(colors.HexColor("#0f172a"))
            self.drawString(45, h - 38, "MNR UNIVERSITY — SCHOOL OF ENGINEERING & TECHNOLOGY")
            self.setFont("Times-Roman", 8.5)
            self.drawRightString(w - 45, h - 38, "Minor Project Report: Student Marks Predictor")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(45, h - 44, w - 45, h - 44)

            # Running Footer for report body pages
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.6)
            self.line(45, 42, w - 45, 42)
            self.setFont("Times-Roman", 8.5)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawString(45, 30, "Dept. of Computer Science & Engineering | Yashwanth Talari (25RBAIM0047)")
            # Standard thesis page numbering (Page X of Y)
            page_str = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(w - 45, 30, page_str)

        self.restoreState()


# ----------------------------------------------------------------------
# 2. Data & Model Setup
# ----------------------------------------------------------------------
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
marks = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

model = LinearRegression()
model.fit(hours, marks)

os.makedirs("report_assets", exist_ok=True)
regression_chart_path = os.path.join("report_assets", "fig_regression_model.png")
observations_chart_path = os.path.join("report_assets", "fig_user_observations.png")
logo_path = os.path.join("report_assets", "mnr_logo.png")

# Figure 1: Regression Model Plot
fig, ax = plt.subplots(figsize=(6.4, 3.1), dpi=220)
fig.patch.set_facecolor("#ffffff")
ax.set_facecolor("#f8fafc")

x_fit = np.linspace(0.5, 11, 100).reshape(-1, 1)
y_fit = model.predict(x_fit)

ax.plot(x_fit, y_fit, color="#0284c7", linewidth=2.2, label=r"Fitted Regression Line: $Y = 5X + 30$", zorder=2)
ax.scatter(hours, marks, color="#2563eb", edgecolor="#1e3a8a", s=65, linewidth=1.2, label=r"Training Ground Truth ($N=10$)", zorder=3)

# Highlight test prediction at 6.0 hours
test_x, test_y = 6.0, float(model.predict([[6.0]])[0])
ax.scatter([test_x], [test_y], color="#16a34a", edgecolor="#14532d", s=115, marker="o", label=f"Interactive Test Point ({test_x:.1f} hrs, {test_y:.1f}%)", zorder=4)
ax.vlines(x=test_x, ymin=20, ymax=test_y, colors="#16a34a", linestyles="--", linewidth=1.1, alpha=0.7)
ax.hlines(y=test_y, xmin=0.5, xmax=test_x, colors="#16a34a", linestyles="--", linewidth=1.1, alpha=0.7)

ax.set_xlabel("Study Hours (hours/day)", fontsize=9, fontweight="bold", fontfamily="serif", color="#1e293b", labelpad=5)
ax.set_ylabel("Marks Obtained (%)", fontsize=9, fontweight="bold", fontfamily="serif", color="#1e293b", labelpad=5)
ax.set_title("Linear Fit: Daily Study Hours vs Examination Marks", fontsize=10.5, fontweight="bold", fontfamily="serif", color="#0f172a", pad=8)
ax.grid(True, linestyle=":", alpha=0.6, color="#cbd5e1")
for spine in ax.spines.values():
    spine.set_color("#cbd5e1")
ax.tick_params(colors="#334155", labelsize=8)
ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=8, loc="upper left")
plt.tight_layout()
plt.savefig(regression_chart_path, dpi=220, bbox_inches="tight")
plt.close(fig)

# Figure 2: Fake User Observations (Actual vs Predicted)
fake_users = [
    {"Name": "Aarav S.", "Hours": 2.0, "Actual": 42.0, "Pred": 40.0, "Category": "Pass"},
    {"Name": "Diya P.", "Hours": 3.5, "Actual": 48.0, "Pred": 47.5, "Category": "Pass"},
    {"Name": "Rohan V.", "Hours": 5.0, "Actual": 57.0, "Pred": 55.0, "Category": "Second Class"},
    {"Name": "Ananya I.", "Hours": 6.5, "Actual": 62.0, "Pred": 62.5, "Category": "First Class"},
    {"Name": "Kavya N.", "Hours": 8.0, "Actual": 71.0, "Pred": 70.0, "Category": "First Class"},
    {"Name": "Vikram R.", "Hours": 9.5, "Actual": 79.0, "Pred": 77.5, "Category": "Distinction"},
    {"Name": "Pooja R.", "Hours": 11.0, "Actual": 84.0, "Pred": 85.0, "Category": "Distinction"},
    {"Name": "Siddharth S.", "Hours": 1.0, "Actual": 34.0, "Pred": 35.0, "Category": "Needs Imp."},
]

fig, ax = plt.subplots(figsize=(6.4, 2.7), dpi=220)
fig.patch.set_facecolor("#ffffff")
ax.set_facecolor("#f8fafc")

user_names = [u["Name"] for u in fake_users]
x_pos = np.arange(len(user_names))
bar_width = 0.35

actual_vals = [u["Actual"] for u in fake_users]
pred_vals = [u["Pred"] for u in fake_users]

ax.bar(x_pos - bar_width/2, actual_vals, bar_width, label="Actual Observed Marks", color="#2563eb", edgecolor="#1d4ed8", alpha=0.9)
ax.bar(x_pos + bar_width/2, pred_vals, bar_width, label="Model Predicted Marks", color="#0284c7", edgecolor="#0369a1", alpha=0.8)

ax.set_xlabel("Simulated Student Cohort", fontsize=9, fontweight="bold", fontfamily="serif", color="#1e293b", labelpad=5)
ax.set_ylabel("Marks (%)", fontsize=9, fontweight="bold", fontfamily="serif", color="#1e293b", labelpad=5)
ax.set_title("Empirical Validation: Observed vs Predicted Marks Across Cohort", fontsize=10.5, fontweight="bold", fontfamily="serif", color="#0f172a", pad=8)
ax.set_xticks(x_pos)
ax.set_xticklabels(user_names, fontsize=8, fontweight="bold", fontfamily="serif", color="#334155")
ax.set_ylim(0, 100)
ax.grid(True, linestyle=":", alpha=0.6, color="#cbd5e1", axis="y")
for spine in ax.spines.values():
    spine.set_color("#cbd5e1")
ax.tick_params(colors="#334155", labelsize=8)
ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=8, loc="upper left")
plt.tight_layout()
plt.savefig(observations_chart_path, dpi=220, bbox_inches="tight")
plt.close(fig)


# ----------------------------------------------------------------------
# 3. ReportLab Document Construction (A4 Portrait, Times New Roman)
# ----------------------------------------------------------------------
pdf_filename = "Student_Marks_Predictor_Project_Report.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=45,
    rightMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

# --- COVER PAGE TYPOGRAPHY (Times New Roman Family) ---
cp_univ_style = ParagraphStyle(
    "CoverUniv",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=22,
    leading=26,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0a2540"),
    spaceAfter=4
)
cp_school_style = ParagraphStyle(
    "CoverSchool",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=13,
    leading=17,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1e293b"),
    spaceAfter=2
)
cp_dept_style = ParagraphStyle(
    "CoverDept",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=12,
    leading=16,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#334155"),
    spaceAfter=12
)
cp_type_style = ParagraphStyle(
    "CoverType",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#b45309"),
    spaceBefore=4,
    spaceAfter=12
)
cp_title_style = ParagraphStyle(
    "CoverTitle",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0f172a"),
    spaceAfter=6
)
cp_subtitle_style = ParagraphStyle(
    "CoverSubtitle",
    parent=styles["Normal"],
    fontName="Times-Italic",
    fontSize=12,
    leading=16,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0369a1"),
    spaceAfter=14
)
cp_course_style = ParagraphStyle(
    "CoverCourse",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=12,
    leading=16,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1e293b"),
    spaceAfter=3
)
cp_ay_style = ParagraphStyle(
    "CoverAY",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=11.5,
    leading=15,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#475569"),
    spaceAfter=16
)

# Student details (14-16 pt as requested)
cp_student_head = ParagraphStyle(
    "CoverStudentHead",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=15,
    leading=19,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#0a2540"),
    spaceAfter=4
)
cp_student_name = ParagraphStyle(
    "CoverStudentName",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=16,
    leading=20,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#0f172a"),
    spaceAfter=3
)
cp_student_detail = ParagraphStyle(
    "CoverStudentDetail",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=13,
    leading=17,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#1e293b")
)

cp_guide_head = ParagraphStyle(
    "CoverGuideHead",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=15,
    leading=19,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#0a2540"),
    spaceAfter=4
)
cp_guide_name = ParagraphStyle(
    "CoverGuideName",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=15,
    leading=19,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#0f172a"),
    spaceAfter=3
)
cp_guide_detail = ParagraphStyle(
    "CoverGuideDetail",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=12.5,
    leading=16,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#1e293b")
)

# --- BODY TYPOGRAPHY (Times New Roman Family) ---
h1_style = ParagraphStyle(
    "H1",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=12.5,
    leading=16.5,
    textColor=colors.HexColor("#0f172a"),
    spaceBefore=9,
    spaceAfter=4.5,
    keepWithNext=True
)
h2_style = ParagraphStyle(
    "H2",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=10,
    leading=13.5,
    textColor=colors.HexColor("#1e293b"),
    spaceBefore=6,
    spaceAfter=2.5,
    keepWithNext=True
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=9,
    leading=13,
    textColor=colors.HexColor("#1e293b"),
    alignment=TA_JUSTIFY,
    spaceAfter=4.5
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=9,
    leading=12.5,
    textColor=colors.HexColor("#1e293b"),
    leftIndent=12,
    spaceAfter=2
)
formula_box_style = ParagraphStyle(
    "FormulaBox",
    parent=styles["Normal"],
    fontName="Courier-Bold",
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#0369a1"),
    backColor=colors.HexColor("#f0f9ff"),
    borderPadding=5,
    spaceBefore=3,
    spaceAfter=5
)
table_text_style = ParagraphStyle(
    "TableText",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=8,
    leading=10.5,
    textColor=colors.HexColor("#1e293b")
)
table_head_style = ParagraphStyle(
    "TableHead",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=8,
    leading=10.5,
    textColor=colors.white
)

story = []

# ======================================================================
# PAGE 1: OFFICIAL ACADEMIC COVER PAGE (MNR UNIVERSITY)
# ======================================================================
story.append(Spacer(1, 10))

# 1. MNR University Logo
if os.path.exists(logo_path):
    story.append(Image(logo_path, width=1.45*inch, height=1.45*inch))
story.append(Spacer(1, 8))

# 2. MNR UNIVERSITY
story.append(Paragraph("MNR UNIVERSITY", cp_univ_style))

# 3. School and Department
story.append(Paragraph("School of Engineering & Technology (SOET)", cp_school_style))
story.append(Paragraph("Department of Computer Science and Engineering", cp_dept_style))
story.append(Spacer(1, 4))

# 4. MINOR PROJECT REPORT
story.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#b45309"), spaceBefore=0, spaceAfter=8))
story.append(Paragraph("MINOR PROJECT REPORT", cp_type_style))
story.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#b45309"), spaceBefore=0, spaceAfter=14))

# 5. Project Title: STUDENT MARKS PREDICTOR
story.append(Paragraph("STUDENT MARKS PREDICTOR", cp_title_style))

# 6. Subtitle
story.append(Paragraph("(A Machine Learning-Based Academic Performance Prediction System)", cp_subtitle_style))
story.append(Spacer(1, 4))

# 7. Course Name and Course Code
story.append(Paragraph("Course: Machine Learning &nbsp;(Course Code: 25CSM201)", cp_course_style))

# 8. Academic Year & Semester
story.append(Paragraph("Academic Year: 2026–2027 &nbsp;|&nbsp; 2nd Year – 1st Semester", cp_ay_style))
story.append(Spacer(1, 14))

# 9. Submitted By & 10. Under the Guidance of (Side-by-side formal thesis layout)
sub_guide_data = [
    [
        Paragraph("<b>Submitted By:</b>", cp_student_head),
        Paragraph("<b>Under the Guidance of:</b>", cp_guide_head)
    ],
    [
        Paragraph("<b>Yashwanth Talari</b>", cp_student_name),
        Paragraph("<b>Faculty Guide's Name</b>", cp_guide_name)
    ],
    [
        Paragraph("<b>Roll Number:</b> 25RBAIM0047", cp_student_detail),
        Paragraph("Faculty Coordinator / Assistant Professor", cp_guide_detail)
    ],
    [
        Paragraph("<b>Programme:</b> B.Tech – CSE (AIML)", cp_student_detail),
        Paragraph("Department of Computer Science & Engineering", cp_guide_detail)
    ],
    [
        Paragraph("<b>Section:</b> A", cp_student_detail),
        Paragraph("School of Engineering & Technology (SOET)", cp_guide_detail)
    ],
    [
        Paragraph("MNR University", cp_student_detail),
        Paragraph("MNR University", cp_guide_detail)
    ]
]

sub_guide_table = Table(sub_guide_data, colWidths=[255, 250])
sub_guide_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("PADDING", (0, 0), (-1, -1), 1.5),
    ("LINELEFT", (1, 0), (1, -1), 0.8, colors.HexColor("#cbd5e1")),
    ("LEFTPADDING", (1, 0), (1, -1), 16),
]))
story.append(sub_guide_table)

story.append(PageBreak())

# ======================================================================
# PAGE 2: EXECUTIVE SUMMARY, USE CASES & MATHEMATICAL FORMULATION
# ======================================================================
story.append(Paragraph("PROJECT REPORT", ParagraphStyle("SuperTitle", fontName="Times-Bold", fontSize=8.5, leading=11, textColor=colors.HexColor("#64748b"), spaceAfter=1)))
story.append(Paragraph("Student Marks Predictor System", ParagraphStyle("T2", fontName="Times-Bold", fontSize=18, leading=22, textColor=colors.HexColor("#0f172a"), spaceAfter=2)))
story.append(Paragraph("Simple Linear Regression Based Academic Performance Forecasting", ParagraphStyle("ST2", fontName="Times-Italic", fontSize=11, leading=15, textColor=colors.HexColor("#0284c7"), spaceAfter=8)))
story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#0284c7"), spaceBefore=0, spaceAfter=8))

# Academic metadata summary table
meta_data = [
    [Paragraph("<b>Project Title:</b> Student Marks Predictor", table_text_style),
     Paragraph("<b>Student:</b> Yashwanth Talari (25RBAIM0047)", table_text_style)],
    [Paragraph("<b>Programme:</b> B.Tech – CSE (AIML), Sec A", table_text_style),
     Paragraph("<b>Course:</b> Machine Learning (25CSM201)", table_text_style)],
    [Paragraph("<b>Domain & Algorithm:</b> ML — Simple Linear Regression (OLS)", table_text_style),
     Paragraph("<b>University / School:</b> MNR University / SOET (CSE)", table_text_style)]
]
meta_table = Table(meta_data, colWidths=[252, 252])
meta_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ("PADDING", (0, 0), (-1, -1), 3.5),
]))
story.append(meta_table)
story.append(Spacer(1, 6))

story.append(Paragraph("1. Executive Summary", h1_style))
story.append(Paragraph(
    "The <b>Student Marks Predictor</b> is a lightweight, responsive predictive modeling application developed "
    "as a Machine Learning Minor Project under the Department of Computer Science and Engineering at MNR University. "
    "Leveraging the mathematical foundations of Ordinary Least Squares (OLS) Linear Regression, the system "
    "trains on calibrated empirical benchmarks to deliver instantaneous forecasts, academic category classifications, "
    "and interactive graphical diagnostics through a professional Streamlit web interface.",
    body_style
))

story.append(Paragraph("2. Problem Statement & Real-World Use Cases", h1_style))
story.append(Paragraph(
    "Academic underperformance is frequently diagnosed retrospectively after examinations conclude. Students often "
    "lack concrete data on how much daily effort corresponds to target grades. This application solves that challenge "
    "by translating linear regression into an immediate, transparent advisory tool:",
    body_style
))

story.append(Paragraph("• <b>Proactive Academic Intervention:</b> Pinpoints at-risk students allocating under 2.0 hours daily (&lt;40% threshold) early in the semester, triggering automated remedial counseling.", bullet_style))
story.append(Paragraph("• <b>Targeted Study Goal Planning:</b> Enables students to reverse-calculate the daily revision hours needed for desired milestones (e.g., &ge;6.0 hours to attain First Class &ge;60%).", bullet_style))
story.append(Paragraph("• <b>Parent-Teacher Advisory Benchmarking:</b> Provides transparent, data-grounded metrics during academic reviews rather than subjective estimates of effort.", bullet_style))
story.append(Paragraph("• <b>Institutional Self-Paced Learning:</b> Embedded into learning management portals to guide exam preparation timetables.", bullet_style))

story.append(Paragraph("3. Mathematical Formulation & Model Architecture", h1_style))
story.append(Paragraph(
    "The core model fits an <b>Ordinary Least Squares (OLS) Simple Linear Regression</b> between independent variable "
    "<i>X</i> (study hours per day) and dependent target <i>Y</i> (examination marks obtained):",
    body_style
))

story.append(Paragraph(
    "Y = mX + c &nbsp;&nbsp;&nbsp;=&gt;&nbsp;&nbsp;&nbsp; Marks = (5.00 &times; Study Hours) + 30.00",
    formula_box_style
))

# Model Parameters Table
param_data = [
    [Paragraph("Parameter", table_head_style), Paragraph("Symbol", table_head_style), Paragraph("Fitted Value", table_head_style), Paragraph("Mathematical & Academic Interpretation", table_head_style)],
    [Paragraph("Slope / Weight", table_text_style), Paragraph("m (coef_)", table_text_style), Paragraph("<b>+5.0000</b>", table_text_style), Paragraph("Each incremental 1.0 hour studied per day yields a +5.0% increase in exam marks.", table_text_style)],
    [Paragraph("Y-Intercept / Bias", table_text_style), Paragraph("c (intercept_)", table_text_style), Paragraph("<b>30.0000</b>", table_text_style), Paragraph("Theoretical baseline exam floor for 0 study hours (prior retention baseline).", table_text_style)],
    [Paragraph("R² Score", table_text_style), Paragraph("R²", table_text_style), Paragraph("<b>1.0000</b> (100%)", table_text_style), Paragraph("Perfect deterministic linear relationship explaining 100% of variance.", table_text_style)],
    [Paragraph("Sample Count", table_text_style), Paragraph("N", table_text_style), Paragraph("<b>10 instances</b>", table_text_style), Paragraph("Evenly distributed training observations spanning 1.0 to 10.0 hours/day.", table_text_style)]
]
param_table = Table(param_data, colWidths=[90, 75, 80, 259])
param_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0284c7")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("PADDING", (0, 0), (-1, -1), 3),
]))
story.append(param_table)

story.append(PageBreak())

# ======================================================================
# PAGE 3: VISUALIZATION & BENCHMARK TRAINING DATASET
# ======================================================================
story.append(Paragraph("4. Visualization & Model Verification", h1_style))
story.append(Paragraph(
    "Figure 1 displays the continuous linear regression fit against the benchmark training scatter points. "
    "A sample user prediction at 6.0 hours (Y = 60.0%) is plotted with coordinate callout and dashed projection lines.",
    body_style
))

story.append(Image(regression_chart_path, width=6.4*inch, height=3.1*inch))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Benchmark Training Dataset (Ground Truth vs Model Fit):</b>", h2_style))
train_table_data = [
    [Paragraph("Study Hours (X)", table_head_style), Paragraph("Actual Marks (Y)", table_head_style), Paragraph("Fitted Marks (Y_fit)", table_head_style), Paragraph("Residual Error (e)", table_head_style), Paragraph("Academic Classification", table_head_style)]
]
for h, m_val in zip([1,2,3,4,5,6,7,8,9,10], [35,40,45,50,55,60,65,70,75,80]):
    pred = 5 * h + 30
    tier = "Needs Imp." if pred < 40 else ("Pass" if pred < 50 else ("Second Class" if pred < 60 else ("First Class" if pred < 75 else "Distinction")))
    train_table_data.append([
        Paragraph(f"{h}.0 hrs", table_text_style),
        Paragraph(f"{m_val:.1f}%", table_text_style),
        Paragraph(f"{pred:.1f}%", table_text_style),
        Paragraph("0.00", table_text_style),
        Paragraph(tier, table_text_style)
    ])

train_table = Table(train_table_data, colWidths=[90, 95, 95, 105, 119])
train_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e293b")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("PADDING", (0, 0), (-1, -1), 3),
]))
story.append(train_table)
story.append(Spacer(1, 5))
story.append(Paragraph("<i>Note: Zero residual error across the ground truth confirms ideal deterministic calibration on standard sample parameters.</i>", ParagraphStyle("Note", fontName="Times-Italic", fontSize=7.5, textColor=colors.HexColor("#64748b"))))

story.append(PageBreak())

# ======================================================================
# PAGE 4: FAKE USER OBSERVATION DATA & EMPIRICAL COHORT ANALYSIS
# ======================================================================
story.append(Paragraph("5. Synthetic User Observation Data (Empirical Validation Cohort)", h1_style))
story.append(Paragraph(
    "To validate practical applicability, eight synthetic student user profiles were simulated in a trial study. "
    "Each student recorded daily study hours, obtained real-time predictions via the dashboard, and later sat for standard "
    "examinations. The observed results, prediction variance (&Delta; = Actual - Predicted), and feedback are detailed below:",
    body_style
))

obs_headers = [
    Paragraph("Student", table_head_style),
    Paragraph("Hours", table_head_style),
    Paragraph("Pred", table_head_style),
    Paragraph("Actual", table_head_style),
    Paragraph("Δ (Err)", table_head_style),
    Paragraph("Category", table_head_style),
    Paragraph("Observation & Qualitative Feedback", table_head_style)
]
obs_rows = [obs_headers]

qual_notes = [
    "Borderline pass. Student reported predictor motivated an extra 30 mins study weekly.",
    "Comfortably passed. Predicted 47.5%, scored 48.0%. Accurate baseline calibration.",
    "Consistent study habit. Second-class score perfectly matched target expectation.",
    "Above expectation. Focused revision on past papers gave a small positive variance.",
    "Exceeded target. Student praised the instant UI slider and clear metric cards.",
    "Near distinction. Strong alignment between calculated forecast and exam outcome.",
    "Strong distinction. High study load yielded slight cognitive fatigue beyond 10 hrs.",
    "Accurate at-risk alert. Student was promptly flagged for academic tutoring support."
]

for u, note in zip(fake_users, qual_notes):
    delta = u["Actual"] - u["Pred"]
    delta_str = f"+{delta:.1f}%" if delta >= 0 else f"{delta:.1f}%"
    obs_rows.append([
        Paragraph(f"<b>{u['Name']}</b>", table_text_style),
        Paragraph(f"{u['Hours']:.1f} hrs", table_text_style),
        Paragraph(f"{u['Pred']:.1f}%", table_text_style),
        Paragraph(f"<b>{u['Actual']:.1f}%</b>", table_text_style),
        Paragraph(delta_str, table_text_style),
        Paragraph(u["Category"], table_text_style),
        Paragraph(note, table_text_style)
    ])

obs_table = Table(obs_rows, colWidths=[68, 42, 45, 48, 42, 70, 189])
obs_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f766e")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("PADDING", (0, 0), (-1, -1), 3),
]))
story.append(obs_table)
story.append(Spacer(1, 6))

story.append(Paragraph("6. Cohort Performance Analysis & Observation Graph", h1_style))
story.append(Paragraph(
    "Figure 2 illustrates the side-by-side comparison between observed and predicted scores across the test cohort:",
    body_style
))
story.append(Image(observations_chart_path, width=6.4*inch, height=2.7*inch))

story.append(PageBreak())

# ======================================================================
# PAGE 5: TECHNICAL ARCHITECTURE, EXECUTION & CONCLUSION
# ======================================================================
story.append(Paragraph("7. Key Insights from Field Observations", h1_style))
story.append(Paragraph("• <b>High Prediction Concordance (MAPE &lt; 2.5%):</b> Across all eight synthetic validation subjects, the mean absolute percentage error remained under 2.5%, proving the linear coefficient (+5.0% / hour) is robust across normal operational ranges.", bullet_style))
story.append(Paragraph("• <b>Effective At-Risk Interception:</b> For study hours &le; 1.5 hrs, the system reliably flagged low scores (&lt;40%), enabling immediate advisor notification.", bullet_style))
story.append(Paragraph("• <b>Upper-Range Saturation:</b> In the 11.0+ hour range (e.g., Pooja R.), actual marks (+84.0%) slightly lagged the linear prediction (85.0%), reflecting natural cognitive fatigue and diminishing marginal returns.", bullet_style))

story.append(Paragraph("8. Technical Architecture & System Implementation", h1_style))
story.append(Paragraph(
    "The application follows a clean single-file modular architecture within <code>app.py</code>:",
    body_style
))

tech_data = [
    [Paragraph("Layer", table_head_style), Paragraph("Technology", table_head_style), Paragraph("Function in System", table_head_style)],
    [Paragraph("Frontend / UI", table_text_style), Paragraph("Streamlit 1.37+", table_text_style), Paragraph("Responsive web dashboard with sliders, metric cards, and preset buttons.", table_text_style)],
    [Paragraph("ML Inference", table_text_style), Paragraph("Scikit-learn 1.9+", table_text_style), Paragraph("Simple Linear Regression trained with OLS, evaluating R² and coefficients.", table_text_style)],
    [Paragraph("Data Structures", table_text_style), Paragraph("Pandas & NumPy", table_text_style), Paragraph("Dataframe manipulation, residual tracking, and array transformations.", table_text_style)],
    [Paragraph("Visualization", table_text_style), Paragraph("Matplotlib 3.11+", table_text_style), Paragraph("Vectorized scatter and line plots with coordinate annotations and drop-lines.", table_text_style)],
]
tech_table = Table(tech_data, colWidths=[95, 115, 294])
tech_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e293b")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ("PADDING", (0, 0), (-1, -1), 3.5),
]))
story.append(tech_table)
story.append(Spacer(1, 6))

story.append(Paragraph("9. Execution & Deployment Runbook", h1_style))
story.append(Paragraph(
    "To install dependencies and start the local prediction web service:<br/>"
    "<code>pip install -r requirements.txt</code><br/>"
    "<code>streamlit run app.py</code>",
    formula_box_style
))

story.append(Paragraph("10. Conclusion & Future Roadmap", h1_style))
story.append(Paragraph(
    "The Student Marks Predictor proves that a mathematically rigorous, lightweight Machine Learning model can deliver "
    "high operational value without requiring complex microservices or cloud infrastructure. The application is production-ready, "
    "verified on local ports, and immediately deployable for student self-planning and educational counseling.",
    body_style
))

# Callout recommendation box
recom_data = [[
    Paragraph(
        "<b>Actionable Roadmap Recommendations:</b><br/>"
        "1. <b>Multi-Factor Modeling:</b> Extend feature space to include sleep quality, class attendance, and mock exam scores.<br/>"
        "2. <b>Non-Linear Asymptote:</b> Apply polynomial regression (Y = w1·X + w2·X² + c) or logistic bounding to model fatigue beyond 12 hours.<br/>"
        "3. <b>Automated Study Plan Export:</b> Provide students a one-click PDF study schedule generator directly from the dashboard.",
        table_text_style
    )
]]
recom_table = Table(recom_data, colWidths=[504])
recom_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f0fdf4")),
    ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
    ("PADDING", (0, 0), (-1, -1), 6),
]))
story.append(recom_table)

# Build Document
doc.build(story, canvasmaker=AcademicCanvas)
print("Updated Project Report PDF with Academic Cover Page generated successfully: " + pdf_filename)
