   M S B A M L   `   `   `  ����  gilbert_tn_gui    gilbert_tn_gui.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   >d2http://schemas.microsoft.com/expression/blend/2008    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	     � Title$  
MainWindow��5   	   $
��86.2��6   $	��206��6*   $	��350��66   $	��350��6E   .��5      � -   5         �Name$
 grid��5       � ColumnDefinitions 5	   
   �� 5
      .+�5   
   �� -   5         ��Name$ namePreview��5      $��10,10,117,32q�6)   $
��Wrap=�6?   ���	#FFD8D8D8$
��Auto=�6j   $
��Auto=�6�    � BindingGroup 5      &   System.Windows.Data.BindingGroup  5      5      �� 5   
   -   5         ��Name$ generateBtn��5      $��Generate��6&   $��
0,0,10,119q�69   $��35��6M   $��Bottom=�6Y   $��Right=�6t   $	��102��6�   6�   �� 5   
   -   5        $ resetBtn��5      $��Reset��6#   $��	0,0,10,81q�63    J� RenderTransformOrigin$ -0.507,-2.571&�6F   $��23��6l   $��Bottom=�6x   $��Right=�6�   $	��102��6�   6�   �� 5   
   -   5         ��Name$ 	lengthBox��5       �� TextWrapping$
 Wrap=�6%   $��
0,0,10,172q�69   $ 
1.25,0.639&�6M   $
��Bold"�6p   $��16(�6�   $��Right=�6�   $��26��6�   $��Bottom=�6�   $��Right=�6�   $	��102��6�   	 J� 	AllowDrop	 .  
 � ToolTip$.
 (The length of the names to be generated.��6  $ �� HorizontalScrollBarVisibility$ Visible=�6G  " �� VerticalScrollBarVisibility$ Disabled=�6o   �� IsUndoEnabled .   �� MaxLines$ 1��6�  �� 5   
   -   5        $ 	exportBtn��5      $��Export��6$   $��	0,0,10,32q�65   $ 0.453,1.057&�6H   $��35��6l   $��Bottom=�6x   $��Right=�6�   $	��102��6�   6�   �� 5   
   -   5         ��Name$ appLogo��5      $	��100��6!   $��
0,0,10,209q�6.   $��Bottom=�6B   $��Right=�6]   $	��100��6y   �� 5   
   -   5        $ 	statusBar��5      $��
10,0,10,10q�6'   $
��Wrap=�6;   $��16��6O   $��Bottom=�6[   5      5      