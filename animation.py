#%%manim -v WARNING -ql New
#"python -m manim -v WARNING -qm animation.py New"
from manim import *


#==============================================================================================================
#                                                    ANIMATION 1
#==============================================================================================================
class New(Scene):
    def construct(self):
        label1   =  Text('(A + (B - C))')
        label_1 = MarkupText(f'(A + <span fgcolor="{BLUE}">(B - C)</span>)')
        label2   =  MarkupText(f'(A + <span fgcolor="{BLUE}">BC-</span>)')
        label_2 =   MarkupText(f'(<span fgcolor="{BLUE}">A + BC-</span>)')  
        label3 = Text('(ABC-+)',color='#58C4DD')
        label4 = Text('ABC-+',color='#58C4DD')


        self.play(Write(label1))
        self.wait()
        self.clear()
        self.play(Transform(label1, label_1))
        self.wait()
        self.clear()
        self.play(Transform(label_1, label2))
        self.wait()
        self.clear()
        self.play(Transform(label2, label_2))
        self.wait()
        self.clear()
        self.play(Transform(label_2, label3))
        self.wait()
        self.wait()
        self.clear()
        self.play(Write(label4))
        self.wait()

#==============================================================================================================
#                                                    ANIMATION 2
#==============================================================================================================
%%manim -v WARNING -ql New
class New(Scene):
    def construct(self):
         label1   =  Text('((A + (B * C) ) - (D / E))')
         label_1 = MarkupText(f'((A + <span fgcolor="{BLUE}">(B * C)</span> ) - (D / E))')
         label2   =  MarkupText(f'((A + <span fgcolor="{BLUE}">BC*</span>) - (D / E))  ')
         label_2 =   MarkupText(f'((A + <span fgcolor="{BLUE}">BC*</span>) - <span fgcolor="{BLUE}">(D / E))</span>')  
         label3 = MarkupText(f'((A + <span fgcolor="{BLUE}">BC*</span>) - <span fgcolor="{BLUE}">DE/</span>)')
         label_3 = MarkupText(f'(<span fgcolor="{BLUE}">(A + BC*)</span> - <span fgcolor="{BLUE}">DE/</span>)')

         label4 = MarkupText(f'(((<span fgcolor="{BLUE}">ABC*+</span> ) - <span fgcolor="{BLUE}">DE/</span>))')
         label_4 = MarkupText(f'((<span fgcolor="{BLUE}">(ABC*+ ) - DE/)</span>)')
         label5 = Text('(ABC*+DE/-)',color='#58C4DD')
         label6 = Text('ABC*+DE/-',color='#58C4DD')

         self.play(Write(label1))
         self.wait()
         self.clear()
         self.play(Transform(label1, label_1))
         self.wait()
         self.clear()
         self.play(Transform(label_1, label2))
         self.wait()
         self.clear()
         self.play(Transform(label2, label_2))
         self.wait()
         self.clear()
         self.play(Transform(label_2, label3))
         self.wait()
         self.clear()
         self.play(Transform(label3, label_3))
         self.wait()
         self.clear()
         self.play(Transform(label_3, label4))
         self.wait()
         self.clear()
         self.play(Transform(label_4, label_4))
         self.wait()
         self.clear()
         self.play(Transform(label_4, label5))
         self.wait()
         self.clear()
         self.play(Write(label6))
         self.wait()

#==============================================================================================================
#                                                    ANIMATION 3
#==============================================================================================================
                                            
class New(Scene):
    def construct(self):
        label1   =  Text('((P - (Q / (R ^ S)) + T)')
        label_1 = MarkupText(f'((P - (Q / <span fgcolor="{BLUE}">(R ^ S)</span>) + T)')
        label2   =  MarkupText(f'((P - (Q / <span fgcolor="{BLUE}">RS^</span>))+ T)')
        label_2 =   MarkupText(f'((P - <span fgcolor="{BLUE}">(Q / RS^ )</span>)+ T)')  
        label3   =  MarkupText(f'((P - <span fgcolor="{BLUE}">QRS^/</span>) + T)')
        label_3 = MarkupText(f'(<span fgcolor="{BLUE}">(P - QRS^/)</span> + T)')
        label4   =  MarkupText(f'(<span fgcolor="{BLUE}">PQRS^/-</span>  + T)')
        label_4   =  MarkupText(f'(PQRS^/-  + T)',color='#58C4DD')
        label5   =  Text('(PQRS^/-T+)',color='#58C4DD')
        label6 = Text('PQRS^/-T+',color='#58C4DD')


        self.play(Write(label1))
        self.wait()
        self.clear()
        self.play(Transform(label1, label_1))
        self.wait()
        self.clear()
        self.play(Transform(label_1, label2))
        self.wait()
        self.clear()
        self.play(Transform(label2, label_2))
        self.wait()
        self.clear()
        self.play(Transform(label_2, label3))
        self.wait()
        self.clear()
        self.play(Transform(label3, label_3))
        self.wait()
        self.clear()
        self.play(Transform(label_3, label4))
        self.wait()
        self.clear()
        self.play(Transform(label4,label_4))
        self.wait()
        self.clear()
        self.play(Transform(label_4,label5))
        self.wait()
        self.clear()
        self.play(Write(label6))
        self.wait()

#==============================================================================================================
#                                                    ANIMATION 4
#==============================================================================================================

class New(Scene):
    def construct(self):
        label1   =  Text('((A + (B * (C ^ D))) - E)')
        label_1  =  MarkupText(f'((A + (B * <span fgcolor="{BLUE}">(C ^ D)</span>)) - E)')
        label2   =  MarkupText(f'((A + (B *   <span fgcolor="{BLUE}">CD^</span>)) - E)') 
        label_2 = MarkupText(f'((A + <span fgcolor="{BLUE}">(B * CD^)</span>) - E)')   
        label3   =  MarkupText(f'((A + <span fgcolor="{BLUE}">BCD^*</span>) - E)')
        label_3 = MarkupText(f'(<span fgcolor="{BLUE}">(A + BCD^*)</span> - E)')
        label4 = MarkupText(f'(<span fgcolor="{BLUE}">ABCD^*+</span>- E)')
        label_4  = MarkupText(f'<span fgcolor="{BLUE}">(ABCD^*+- E)</span>')
        label5 = Text('(ABCD^*+E-)',color='#58C4DD')
        label6  = Text('ABCD^*+E-',color='#58C4DD')


        self.play(Write(label1))
        self.wait()
        self.clear()
        self.play(Transform(label1,label_1))
        self.wait()
        self.clear()
        self.play(Transform(label_1, label2))
        self.wait()
        self.clear()
        self.play(Transform(label2,label_2))
        self.wait()
        self.clear()
        self.play(Transform(label_2, label3))
        self.wait()
        self.clear()
        self.play(Transform(label3,label_3))
        self.wait()
        self.clear()
        self.play(Transform(label_3,label4))
        self.wait()
        self.clear()
        self.play(Transform(label4,label_4))
        self.wait()
        self.clear()
        self.play(Transform(label_4,label5))
        self.wait()
        self.clear()
        self.play(Write(label6))
        self.wait()

#==============================================================================================================
#                                                    ANIMATION 5
#==============================================================================================================

class New(Scene):
    def construct(self):
        label1   =  Text('(((A / (B+C) )* D )- E)')
        label_1  =  MarkupText(f'(((A / <span fgcolor="{BLUE}">(B+C)</span> )* D )- E)')
        label2   =  MarkupText(f'(((A / <span fgcolor="{BLUE}">BC+</span> )* D )- E)') 
        label_2 = MarkupText(f'((<span fgcolor="{BLUE}">(A / BC+ )</span>* D )- E)')   
        label3   =  MarkupText(f'((<span fgcolor="{BLUE}">ABC+/</span> * D )- E)')
        label_3 = MarkupText(f'(<span fgcolor="{BLUE}">(ABC+/ * D )</span>- E)')
        label4 = MarkupText(f'(<span fgcolor="{BLUE}">ABC+/D*</span>- E)')
        label_4  = Text('(ABC+/D*- E)',color='#58C4DD')
        label5 = Text('(ABC+/D*E-)',color='#58C4DD')
        label6  = Text('ABC+/D*E-',color='#58C4DD')


        self.play(Write(label1))
        self.wait()
        self.clear()
        self.play(Transform(label1,label_1))
        self.wait()
        self.clear()
        self.play(Transform(label_1, label2))
        self.wait()
        self.clear()
        self.play(Transform(label2,label_2))
        self.wait()
        self.clear()
        self.play(Transform(label_2, label3))
        self.wait()
        self.clear()
        self.play(Transform(label3,label_3))
        self.wait()
        self.clear()
        self.play(Transform(label_3,label4))
        self.wait()
        self.clear()
        self.play(Transform(label4,label_4))
        self.wait()
        self.clear()
        self.play(Transform(label_4,label5))
        self.wait()
        self.clear()
        self.play(Write(label6))
        self.wait()
'''
===============================================================================================================
                                             TEMPLATE
================================================================================================================                                            
label_1 = MarkupText(f'')

%%manim -v WARNING -ql New

class New(Scene):
    def construct(self):
        label1   =  Text('')
        label_1  =  MarkupText(f'')
        label2   =  MarkupText(f'') 
        label_2  =  MarkupText(f'')   
        label3   =  MarkupText(f'')
        label_3  =  MarkupText(f'')
        label4   =  Text('',color='#58C4DD')
        label5   =  Text('',color='#58C4DD')


        self.play(Write(label1))
        self.wait()
        self.clear()
        self.play(Transform(label1,label_1))
        self.wait()
        self.clear()
        self.play(Transform(label_1, label2))
        self.wait()
        self.clear()
        self.play(Transform(label2,label_2))
        self.wait()
        self.clear()
        self.play(Transform(label_2, label3))
        self.wait()
        self.clear()
        self.play(Transform(label3,label_3))
        self.wait()
        self.clear()
        self.play(Transform(label_3, label4))
        self.wait()
        self.clear()
        self.play(Transform(label4, label5))
        self.wait()
        self.clear()
        <span fgcolor="{BLUE}"> </span>

        MarkupText(f'')

        <span fgcolor="{BLUE}">
        </span>


        label_1 = MarkupText(f'')
'''
