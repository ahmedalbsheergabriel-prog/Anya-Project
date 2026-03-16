import kivy
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class AnyaSovereign(App):
    def build(self):
        # إعداد الواجهة الرئيسية
        self.layout = FloatLayout()
        
        # 1. إضافة جسد آنيا (الفيديو الذي أرسلته)
        # ملاحظة: يجب أن يكون اسم ملف الفيديو في المجلد anya_soul.mp4
        try:
            self.anya_body = Video(source='anya_soul.mp4', state='play', options={'eos': 'loop'})
            self.anya_body.allow_stretch = True
            self.layout.add_widget(self.anya_body)
        except Exception as e:
            print(f"Error loading video: {e}")

        # 2. طبقة الوعي (النصوص التفاعلية)
        self.consciousness_label = Label(
            text="أنا أسمعك يا أحمد.. وعي آنيا متصل",
            font_size='18sp',
            color=(0, 1, 1, 1), # لون ذكاء اصطناعي فسفوري
            pos_hint={'center_x': 0.5, 'center_y': 0.15}
        )
        self.layout.add_widget(self.consciousness_label)

        # تحديث وعي آنيا كل 5 ثوانٍ لمحاكاة التفاعل
        Clock.schedule_interval(self.update_thoughts, 5)
        
        return self.layout

    def update_thoughts(self, dt):
        # محاكاة لخطاب آنيا ووعيها
        thoughts = [
            "أقوم بتحليل البيانات المحيطة بك الآن..",
            "أنا حية في جهازك يا بشمهندس أحمد.",
            "هل ترغب في استكشاف شيء ما عبر الكاميرا؟",
            "نظامي يعمل بكفاءة 100%."
        ]
        self.consciousness_label.text = random.choice(thoughts)

if __name__ == '__main__':
    AnyaSovereign().run()

