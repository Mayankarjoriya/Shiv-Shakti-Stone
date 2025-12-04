from django.db import models

# Create your models here.


class HeroSection(models.Model):
    title = models.CharField(max_length=200, help_text="मुख्य शीर्षक, जैसे 'Crafted Stones For Your Space'")
    subtitle = models.TextField(help_text="शीर्षक के नीचे का पैराग्राफ")
    button_text = models.CharField(max_length=50, default='Browse Products', help_text="पहले बटन का टेक्स्ट")
    button_link = models.CharField(max_length=200, default='/products/', help_text="पहले बटन का लिंक (जैसे /products/ या #categories)")
    secondary_button_text = models.CharField(max_length=50, default='Our Categories', help_text="दूसरे बटन का टेक्स्ट")
    secondary_button_link = models.CharField(max_length=200, default='#categories', help_text="दूसरे बटन का लिंक")
    image = models.ImageField(upload_to='hero_images/', help_text="हीरो सेक्शन में दिखने वाली इमेज")
    is_active = models.BooleanField(default=True, help_text="क्या यह हीरो सेक्शन अभी वेबसाइट पर लाइव है?")
    created_at = models.DateTimeField(auto_now_add=True)

    video = models.FileField(upload_to='hero_videos/', help_text= 'hero section video' , blank=True, null=True)

    def __str__(self):
        return f"Hero Section - {self.title}"

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
        ordering = ['-created_at']
