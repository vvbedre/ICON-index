import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
import base64

class ICONCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("ICON Orthodontic Assessment Tool")
        self.root.geometry("1000x850")
        
        # Create main container
        self.mainframe = ttk.Frame(self.root, padding="20")
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(self.mainframe, text="ICON (Index of Complexity, Outcome and Need)", 
                 font=('Helvetica', 14, 'bold')).grid(column=0, row=0, columnspan=4, pady=10)
        
        # Description
        desc = """The ICON index assesses orthodontic treatment need, complexity, and likely outcome.
Developed by Daniels and Richmond (2000) through international consensus of 97 orthodontists.
It evaluates dental aesthetics, crossbites, crowding, buccal occlusion, and vertical relationships."""
        ttk.Label(self.mainframe, text=desc, wraplength=900).grid(column=0, row=1, columnspan=4, pady=10)
        
        # Create notebook for different sections
        self.notebook = ttk.Notebook(self.mainframe)
        self.notebook.grid(column=0, row=2, columnspan=4, pady=10, sticky=(tk.W, tk.E))
        
        # Create assessment frames
        self.create_aesthetic_frame()
        self.create_crossbite_frame()
        self.create_crowding_frame()
        self.create_buccal_frame()
        self.create_vertical_frame()
        self.create_results_frame()
        
        # Set default values
        self.set_default_values()
    
    def create_aesthetic_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Dental Aesthetics")
        
        # Dental aesthetics image
        try:
            img_data = base64.b64decode("""R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7""")
            img = Image.open(io.BytesIO(img_data))
            photo = ImageTk.PhotoImage(img)
            img_label = ttk.Label(frame, image=photo)
            img_label.image = photo
            img_label.grid(column=0, row=0, columnspan=2, pady=5)
        except:
            pass
        
        ttk.Label(frame, text="Dental Aesthetic Component (DAC):", font=('Helvetica', 10, 'bold')).grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=5)
        
        # DAC scale description
        dac_desc = """Score based on the most similar photograph from the 10-grade Dental Aesthetic Component scale:
Grade 1-2: Minor or no need
Grade 3: Borderline need
Grade 4-5: Definite need"""
        ttk.Label(frame, text=dac_desc, wraplength=600).grid(column=0, row=2, columnspan=2, sticky=tk.W, pady=5)
        
        # DAC selection
        ttk.Label(frame, text="Select DAC Grade (1-10):").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.dac_grade = ttk.Combobox(frame, values=list(range(1, 11)), width=5)
        self.dac_grade.grid(column=1, row=3, sticky=tk.W, pady=5)
        
        # Info button
        ttk.Button(frame, text="View DAC Scale", command=self.show_dac_scale).grid(column=0, row=4, columnspan=2, pady=10)
    
    def create_crossbite_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Crossbite")
        
        ttk.Label(frame, text="Crossbite Assessment", font=('Helvetica', 10, 'bold')).grid(column=0, row=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Crossbite description
        crossbite_desc = """Assess presence of anterior or posterior crossbites:
- No crossbite: 0 points
- Crossbite ≤1mm RCP-ICP discrepancy: 5 points
- Crossbite >1mm RCP-ICP discrepancy: 10 points
(RCP=Retruded Contact Position, ICP=Intercuspal Position)"""
        ttk.Label(frame, text=crossbite_desc, wraplength=600).grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Crossbite selection
        ttk.Label(frame, text="Crossbite Severity:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.crossbite = ttk.Combobox(frame, values=["No crossbite", "Crossbite ≤1mm RCP-ICP", "Crossbite >1mm RCP-ICP"], width=25)
        self.crossbite.grid(column=1, row=2, sticky=tk.W, pady=5)
        
        # Additional crossbite questions
        ttk.Label(frame, text="Posterior Lingual Crossbite with no functional contact?").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.lingual_crossbite = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.lingual_crossbite.grid(column=1, row=3, sticky=tk.W, pady=5)
    
    def create_crowding_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Crowding/Spacing")
        
        ttk.Label(frame, text="Upper Arch Crowding/Spacing", font=('Helvetica', 10, 'bold')).grid(column=0, row=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Crowding description
        crowding_desc = """Measure the most crowded or spaced segment in the upper arch:
- No crowding/spacing: 0 points
- ≤3mm discrepancy: 5 points
- >3mm discrepancy: 10 points
Also assess for impacted teeth or other anomalies"""
        ttk.Label(frame, text=crowding_desc, wraplength=600).grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Upper arch selection
        ttk.Label(frame, text="Upper Arch Discrepancy:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.upper_arch = ttk.Combobox(frame, values=["No discrepancy", "≤3mm discrepancy", ">3mm discrepancy"], width=20)
        self.upper_arch.grid(column=1, row=2, sticky=tk.W, pady=5)
        
        # Additional anomalies
        ttk.Label(frame, text="Additional Anomalies:", font=('Helvetica', 10, 'bold')).grid(column=0, row=3, columnspan=2, sticky=tk.W, pady=5)
        
        ttk.Label(frame, text="Impacted teeth (except 3rd molars):").grid(column=0, row=4, sticky=tk.W, pady=2)
        self.impacted = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.impacted.grid(column=1, row=4, sticky=tk.W, pady=2)
        
        ttk.Label(frame, text="Supernumerary teeth:").grid(column=0, row=5, sticky=tk.W, pady=2)
        self.supernumerary = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.supernumerary.grid(column=1, row=5, sticky=tk.W, pady=2)
        
        ttk.Label(frame, text="Submerged deciduous teeth:").grid(column=0, row=6, sticky=tk.W, pady=2)
        self.submerged = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.submerged.grid(column=1, row=6, sticky=tk.W, pady=2)
        
        ttk.Label(frame, text="Extensive hypodontia (>1 tooth/quadrant):").grid(column=0, row=7, sticky=tk.W, pady=2)
        self.hypodontia = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.hypodontia.grid(column=1, row=7, sticky=tk.W, pady=2)
    
    def create_buccal_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Buccal Occlusion")
        
        ttk.Label(frame, text="Buccal Segment Anteroposterior Relationship", font=('Helvetica', 10, 'bold')).grid(column=0, row=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Buccal occlusion description
        buccal_desc = """Assess the worst side for buccal segment relationship:
- Normal occlusion: 0 points
- Up to 1/2 unit discrepancy: 5 points
- >1/2 unit discrepancy: 10 points
(1 unit = full cusp width)"""
        ttk.Label(frame, text=buccal_desc, wraplength=600).grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Buccal occlusion selection
        ttk.Label(frame, text="Worst Buccal Segment Relationship:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.buccal_occlusion = ttk.Combobox(frame, values=["Normal", "≤1/2 unit discrepancy", ">1/2 unit discrepancy"], width=25)
        self.buccal_occlusion.grid(column=1, row=2, sticky=tk.W, pady=5)
    
    def create_vertical_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Vertical Relationship")
        
        ttk.Label(frame, text="Anterior Vertical Relationship", font=('Helvetica', 10, 'bold')).grid(column=0, row=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Vertical description
        vertical_desc = """Assess anterior openbite or deep overbite:
- Normal overbite (0-3.5mm): 0 points
- Openbite 1-2mm or deep bite ≥3.5mm no trauma: 5 points
- Openbite >2mm or deep bite with trauma: 10 points"""
        ttk.Label(frame, text=vertical_desc, wraplength=600).grid(column=0, row=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Vertical relationship selection
        ttk.Label(frame, text="Anterior Vertical Relationship:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.vertical = ttk.Combobox(frame, values=["Normal", "Openbite 1-2mm or deep bite ≥3.5mm", "Openbite >2mm or deep bite with trauma"], width=40)
        self.vertical.grid(column=1, row=2, sticky=tk.W, pady=5)
        
        # Additional vertical questions
        ttk.Label(frame, text="Extreme Lateral Openbite >4mm:").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.lateral_openbite = ttk.Combobox(frame, values=["No", "Yes"], width=5)
        self.lateral_openbite.grid(column=1, row=3, sticky=tk.W, pady=5)
    
    def create_results_frame(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Results")
        
        # Calculate button
        ttk.Button(frame, text="Calculate ICON Score", command=self.calculate_icon).grid(column=0, row=0, columnspan=2, pady=10)
        
        # Results display
        self.results_text = tk.Text(frame, wrap=tk.WORD, width=80, height=20, state=tk.DISABLED)
        self.results_text.grid(column=0, row=1, columnspan=2, pady=10)
        
        # Info button
        ttk.Button(frame, text="ICON Interpretation Guide", command=self.show_icon_guide).grid(column=0, row=2, columnspan=2, pady=10)
    
    def set_default_values(self):
        # Set default values for demonstration
        self.dac_grade.set(4)
        self.crossbite.set("No crossbite")
        self.lingual_crossbite.set("No")
        self.upper_arch.set(">3mm discrepancy")
        self.impacted.set("No")
        self.supernumerary.set("No")
        self.submerged.set("No")
        self.hypodontia.set("No")
        self.buccal_occlusion.set(">1/2 unit discrepancy")
        self.vertical.set("Normal")
        self.lateral_openbite.set("No")
    
    def calculate_icon(self):
        try:
            # Initialize score
            total_score = 0
            components = []
            
            # 1. Dental Aesthetic Component (DAC) - max 100 points
            dac_grade = int(self.dac_grade.get())
            dac_score = (dac_grade - 1) * 10  # Grade 1=0, Grade 10=90
            components.append(f"Dental Aesthetics (Grade {dac_grade}): {dac_score} points")
            total_score += dac_score
            
            # 2. Crossbite - max 10 points
            crossbite = self.crossbite.get()
            if crossbite == "Crossbite ≤1mm RCP-ICP":
                cross_score = 5
            elif crossbite == "Crossbite >1mm RCP-ICP":
                cross_score = 10
            else:
                cross_score = 0
            
            # Check for lingual crossbite (additional 10 points)
            if self.lingual_crossbite.get() == "Yes":
                cross_score = max(cross_score, 10)
                components.append("Posterior Lingual Crossbite: 10 points")
            else:
                components.append(f"Crossbite: {cross_score} points")
            
            total_score += cross_score
            
            # 3. Upper Arch Crowding/Spacing - max 10 points
            upper_arch = self.upper_arch.get()
            if upper_arch == "≤3mm discrepancy":
                crowding_score = 5
            elif upper_arch == ">3mm discrepancy":
                crowding_score = 10
            else:
                crowding_score = 0
            components.append(f"Upper Arch: {crowding_score} points")
            total_score += crowding_score
            
            # 4. Additional Anomalies - various points
            anomaly_score = 0
            
            if self.impacted.get() == "Yes":
                anomaly_score = max(anomaly_score, 20)
                components.append("Impacted Teeth: 20 points")
            
            if self.supernumerary.get() == "Yes":
                anomaly_score = max(anomaly_score, 20)
                components.append("Supernumerary Teeth: 20 points")
            
            if self.submerged.get() == "Yes":
                anomaly_score = max(anomaly_score, 20)
                components.append("Submerged Deciduous Teeth: 20 points")
            
            if self.hypodontia.get() == "Yes":
                anomaly_score = max(anomaly_score, 20)
                components.append("Extensive Hypodontia: 20 points")
            
            total_score += anomaly_score
            
            # 5. Buccal Occlusion - max 10 points
            buccal = self.buccal_occlusion.get()
            if buccal == "≤1/2 unit discrepancy":
                buccal_score = 5
            elif buccal == ">1/2 unit discrepancy":
                buccal_score = 10
            else:
                buccal_score = 0
            components.append(f"Buccal Occlusion: {buccal_score} points")
            total_score += buccal_score
            
            # 6. Vertical Relationship - max 10 points
            vertical = self.vertical.get()
            if vertical == "Openbite 1-2mm or deep bite ≥3.5mm":
                vertical_score = 5
            elif vertical == "Openbite >2mm or deep bite with trauma":
                vertical_score = 10
            else:
                vertical_score = 0
            
            # Check for extreme lateral openbite (additional 10 points)
            if self.lateral_openbite.get() == "Yes":
                vertical_score = max(vertical_score, 10)
                components.append("Extreme Lateral Openbite: 10 points")
            else:
                components.append(f"Vertical Relationship: {vertical_score} points")
            
            total_score += vertical_score
            
            # Determine Treatment Need
            if total_score >= 43:
                treatment_need = "Definite Need for Treatment (Grade 4-5)"
            elif total_score >= 31:
                treatment_need = "Borderline Need (Grade 3)"
            else:
                treatment_need = "Little or No Need (Grade 1-2)"
            
            # Display results
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            
            self.results_text.insert(tk.END, "ICON COMPONENT SCORES:\n", 'header')
            for component in components:
                self.results_text.insert(tk.END, f"- {component}\n")
            
            self.results_text.insert(tk.END, "\nTOTAL ICON SCORE: ", 'header')
            self.results_text.insert(tk.END, f"{total_score} points\n\n", 'score')
            
            self.results_text.insert(tk.END, "TREATMENT NEED ASSESSMENT:\n", 'header')
            self.results_text.insert(tk.END, f"{treatment_need}\n\n", 'assessment')
            
            # Add interpretation
            self.results_text.insert(tk.END, "INTERPRETATION:\n", 'header')
            if total_score >= 43:
                self.results_text.insert(tk.END, """The patient has a definite need for orthodontic treatment.
This includes cases with severe malocclusions that are likely to:
- Affect dental health and function
- Impact psychosocial well-being
- Require complex treatment planning""")
            elif total_score >= 31:
                self.results_text.insert(tk.END, """The patient is in the borderline range for treatment need.
Consider:
- Patient's concerns and expectations
- Potential benefits versus risks
- Alternative treatment options
A detailed case assessment is recommended.""")
            else:
                self.results_text.insert(tk.END, """The patient has little or no objective need for orthodontic treatment.
Treatment would be primarily for aesthetic improvement.
Consider whether the benefits justify the costs and risks.""")
            
            self.results_text.tag_config('header', font=('Helvetica', 10, 'bold'))
            self.results_text.tag_config('score', font=('Helvetica', 12, 'bold'), foreground='blue')
            self.results_text.tag_config('assessment', font=('Helvetica', 11, 'bold'), foreground='green')
            self.results_text.config(state=tk.DISABLED)
        
        except ValueError:
            messagebox.showerror("Error", "Please complete all assessment fields with valid values.")
    
    def show_dac_scale(self):
        dac_info = """Dental Aesthetic Component (DAC) Scale (1-10):

Grade 1: Extremely minor malocclusions (displacements <1mm)
Grade 2: Minor malocclusions (displacements 1-2mm, overjet 3.5-6mm)
Grade 3: Borderline need (displacements 2-4mm, overjet 5-6mm)
Grade 4: Definite need (displacements >4mm, overjet >6mm)
Grade 5: Severe need (overjet >9mm, reverse overjet >3.5mm)

Grades 6-10 represent increasing severity of:
- Openbites
- Deep bites with trauma
- Crossbites with functional shifts
- Impacted teeth
- Other severe anomalies"""
        
        messagebox.showinfo("DAC Scale Information", dac_info)
    
    def show_icon_guide(self):
        icon_guide = """ICON SCORE INTERPRETATION GUIDE:

Treatment Need Categories:
- <31 points: Little or no need (Grade 1-2)
- 31-42 points: Borderline need (Grade 3)
- ≥43 points: Definite need (Grade 4-5)

Component Weightings:
1. Dental Aesthetics (0-90 points): Based on DAC grade
2. Crossbite (0-10 points): Functional assessment
3. Upper Arch (0-10 points): Crowding/spacing severity
4. Additional Anomalies (0-20 points): Impacted teeth, hypodontia, etc.
5. Buccal Occlusion (0-10 points): AP relationship
6. Vertical Relationship (0-10 points): Openbite/deep bite

Clinical Applications:
- Objective treatment need assessment
- Case prioritization
- Treatment complexity evaluation
- Outcome comparison

Limitations:
- Doesn't assess skeletal relationships
- Doesn't evaluate facial aesthetics
- Doesn't consider patient preferences"""
        
        messagebox.showinfo("ICON Interpretation Guide", icon_guide)

if __name__ == "__main__":
    root = tk.Tk()
    app = ICONCalculator(root)
    root.mainloop()