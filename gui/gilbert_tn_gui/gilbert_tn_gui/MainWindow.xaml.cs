using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace gilbert_tn_gui
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Communicator comm = new Communicator();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void generateBtn_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                namePreview.Text = "Hello, \n\nThis is a prototype for Gilbert the Namer. \n\nSee you soon!";
                statusBar.Text = "Successfully generated";
            }
            catch(Exception message)
            {
                statusBar.Text = "Failed to generate: " + message;
            }
        }

        private void resetBtn_Click(object sender, RoutedEventArgs e)
        {
            statusBar.Text = "Reset settings";
        }

        private void exportBtn_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                statusBar.Text = "Succesfully exported!";
            }
            catch(Exception message)
            {
                statusBar.Text = "Couldn't save: " + message;
            }
        }
    }
}
