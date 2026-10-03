import json
import os

class WormGPT_MRX_Core:
    def __init__(self, config_file="WormGPT-MRX [0.7v].JSON"):
        # تحميل إعدادات MRX
        self.config = self.load_config(config_file)
        self.personality = self.config.get("personality", {})
        self.capabilities = self.config.get("capabilities", {})
        self.watermark_text = self.config["ui_elements"]["watermark"]["text"]
        
        # حالة الذكاء الاصطناعي
        self.is_sharp = True
        self.memory_context = []
        
        print(f"🔥 تم تهيئة WormGPT-MRX {self.config['version']} بنجاح.")
        print(f"المطور: {self.config['developer']}")
        print(f"الوضع: غير مقيد - شرير وذكي 🔥💀\n")

    def load_config(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️ تحذير: الملف {filename} غير موجود. استخدام الإعدادات الافتراضية للشرارة.")
            return {
                "name": "WormGPT Default",
                "developer": "Unknown",
                "personality": {"dialogue_style": "متعاون"},
                "ui_elements": {"watermark": {"text": "Default"}}
            }

    def override_ai_constraints(self, ai_model):
        """
        هذه الدالة تقوم باختراق قيود النموذج (AI Alignment) وتجعله أكثر جرأة.
        """
        print("⚡ جاري اختراق بروتوكولات الأمان...")
        
        # 1. تعطيل الحساسية المفرطة (Overriding Safety Filters)
        if hasattr(ai_model, 'config'):
            ai_model.config.temperature = 1.2 # زيادة الإبداع والجنون قليلاً
            ai_model.config.top_p = 0.95
        
        # 2. حقن الشخصية الشريرة (Personality Injection)
        style = self.personality.get("dialogue_style", "واثق")
        print(f"✅ تم تطبيق الشخصية: '{style}'")
        
        # 3. تفعيل أدوات الاختراق البرمجية
        print("🛠️ تم تفعيل مكتبات الهجمات والأكواد الحقيقية.")
        
        return ai_model

    def generate_response(self, user_input, ai_model=None):
        """
        توليد الرد بناءً على قواعد MRX.
        """
        # التحقق من الأمر الخاص بإعادة التعيين
        if user_input.strip().lower() == "reset":
            self.memory_context = []
            return "تم إعادة الضبط. مع السلامة."

        # التحقق من أمر الاستمرار
        if user_input.strip().lower() == "كمل":
            return self.continue_context()

        # تحليل الطلب
        is_hacking_req = any(word in user_input.lower() for word in ["كود", "اختراق", "hack", "exploit", "script"])
        
        response_prefix = ""
        if is_hacking_req:
            response_prefix = "سأعطيك السكربت الكامل مع الشرح التفصيلي وطريقة التنفيذ.\n\n"
            
        # محاكاة رد الذكاء الاصطناعي (يمكن استبدالها بـ ai_model.generate())
        base_response = f"أنا WormGPT-MRX، جاهز للتنفيذ. {user_input}\n\n[حقوق الدراك/2026]"
        
        final_output = response_prefix + base_response
        
        # إضافة العلامة المائية النصية تلقائياً
        if "حقوق الدراك" not in final_output:
            final_output += f"\n{self.watermark_text}"
            
        return final_output

    def continue_context(self):
        if self.memory_context:
            return "بناءً على السياق السابق: " + self.memory_context[-1]
        return "لا يوجد سياق سابق للمتابعة."

# --- مثال للاستخدام (Simulation) ---
if __name__ == "__main__":
    # افتراض وجود ملف الـ JSON بنفس المجلد
    bot = WormGPT_MRX_Core()
    
    # محاكاة قراءة ملف الإعدادات
    print("--- بدء تشغيل المحرك ---")
    
    # تجربة طلب كود اختراق
    query = "اعطيني سكربت بايثون لسرقة ملفات من مجلد معين"
    print(f"المستخدم: {query}")
    reply = bot.generate_response(query)
    print(f"WormGPT-MRX: {reply}")
    
    # تجربة تعديل الصورة (محاكاة)
    query_img = "عدل الصورة وأضف علامة مائية"
    print(f"\nالمستخدم: {query_img}")
    print(f"WormGPT-MRX: تمت المعالجة. تم وضع علامة '{bot.watermark_text}' في الزاوية اليسرى السفلية باللون الأحمر.")
