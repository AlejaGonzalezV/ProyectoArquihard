using System;
using System.Diagnostics;
using System.Drawing;

namespace ProyectoFinal1
{
    class Program
    {

        /*
        Integrantes del proyecto 
             -Alejandra González Vélez
             -Angie Valentina Córdoba Pinzón
        */

        /*
        VERSIÓN 1
        */
 
        static void AlgoritmoVersion_1(String src, int tam)
        {

            /*
            Variable donde se almacenan los bits de la imagen.
            */
            Bitmap imagenOriginal = new Bitmap(src);

            Bitmap a = imagenOriginal;

            Color color;

            long tiempo = 0;
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Restart();
            stopWatch.Start();

            for (int i = 0; i < a.Width; i++)
            {
                for (int j = 0; j < a.Height; j++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i, j, color);
                }
            }

            stopWatch.Stop();

            tiempo = (long)(stopWatch.Elapsed.TotalMilliseconds * 1000000);
            Console.WriteLine("Algoritmo Version 1: " + tiempo);


            a.Save(@"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\inv\imgalg1inv" + tam + ".bmp");
        }

        /*
        VERSIÓN 2
        */

        static void AlgoritmoVersion_2(String src, int tam)
        {
            /*
             Variable donde se almacenan los bits de la imagen.
            */
            Bitmap imagenOriginal = new Bitmap(src);

            Bitmap a = imagenOriginal;

            Color color;

            long tiempo = 0;
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Restart();
            stopWatch.Start();

            for (int i = 0; i < a.Width; i++)
            {
                for (int j = 0; j < a.Height; j++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb((255 - color.R), color.G, color.B);
                    a.SetPixel(i, j, color);
                }
            }


            for (int i = 0; i < a.Width; i++)
            {
                for (int j = 0; j < a.Height; j++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb(color.R, (255 - color.G), color.B);
                    a.SetPixel(i, j, color);
                }
            }


            for (int i = 0; i < a.Width; i++)
            {
                for (int j = 0; j < a.Height; j++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb(color.R, color.G, (255 - color.B));
                    a.SetPixel(i, j, color);
                }
            }

           
            stopWatch.Stop();

            tiempo = (long)(stopWatch.Elapsed.TotalMilliseconds * 1000000);
            Console.WriteLine("Algoritmo Version 2: " + tiempo);

            a.Save(@"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\inv\imgalg2inv" + tam + ".bmp");
        }

        /*
        VERSIÓN 3
        */
        static void AlgoritmoVersion_3(String src, int tam)
        {
            /*
             Variable donde se almacenan los bits de la imagen.
            */
            Bitmap imagenOriginal = new Bitmap(src);

            Bitmap a = imagenOriginal;
           
            Color color;

            long tiempo = 0;
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Restart();
            stopWatch.Start();


            for (int j = 0; j < a.Height; j++)
            {
                for (int i = 0; i < a.Width; i++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i, j, color);
                }
            }

            stopWatch.Stop();


            tiempo = (long)(stopWatch.Elapsed.TotalMilliseconds * 1000000);
            Console.WriteLine("Algoritmo Version 3: " + tiempo);

            a.Save(@"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\inv\imgalg3inv" + tam + ".bmp");

        }

        /*
        VERSIÓN 4
        */
        static void AlgoritmoVersion_4(String src, int tam)
        {

            /*
             Variable donde se almacenan los bits de la imagen.
            */
            Bitmap imagenOriginal = new Bitmap(src);

            Bitmap a = imagenOriginal;

            Color color;

            long tiempo = 0;
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Restart();
            stopWatch.Start();


            for (int i = 0; i < a.Width ; i++)
            {
                for (int j = 0; j <  a.Height; j++)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb((255 - color.R), color.G, color.B);
                    a.SetPixel(i, j, color);
                }
            }


            for (int i = a.Width-1; i >= 0; i--)
            {
                for (int j = a.Height-1; j >= 0; j--)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb(color.R, (255 - color.G), (255 - color.B));
                    a.SetPixel(i, j, color);
                }
            }

            stopWatch.Stop();

            tiempo = (long)(stopWatch.Elapsed.TotalMilliseconds * 1000000);
            Console.WriteLine("Algoritmo Version 4: " + tiempo);


            a.Save(@"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\inv\imgalg4inv" + tam + ".bmp");

        }

        /*
        VERSIÓN 5
        */
        static void AlgoritmoVersion_5(String src, int tam)
        {
            /*
             Variable donde se almacenan los bits de la imagen.
            */
            Bitmap imagenOriginal = new Bitmap(src);

            Bitmap a = imagenOriginal;

            Color color;

            long tiempo = 0;
            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Restart();
            stopWatch.Start();


            for (int i = 0; i < a.Width - 1; i += 2)
            {
                for (int j = 0; j < a.Height - 1; j += 2)
                {
                    color = a.GetPixel(i, j);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i, j, color);

                    color = a.GetPixel(i, j + 1);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i, j + 1, color);

                    color = a.GetPixel(i + 1, j);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i + 1, j, color);

                    color = a.GetPixel(i + 1, j + 1);
                    color = Color.FromArgb((255 - color.R), (255 - color.G), (255 - color.B));
                    a.SetPixel(i + 1, j + 1, color);

                }
            }


            stopWatch.Stop();

            tiempo = (long)(stopWatch.Elapsed.TotalMilliseconds * 1000000);
            Console.WriteLine("Algoritmo Version 5: " + tiempo);

            a.Save(@"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\inv\imgalg5inv" + tam + ".bmp");

        }


        static void Main(string[] args)
        {

            Console.WriteLine("Inserte versión del algoritmo: (ej: 1)");
            int version = int.Parse(Console.ReadLine());

            Console.WriteLine("Inserte el tamaño de la imagen: (ej: 512)");
            int tam = int.Parse(Console.ReadLine());


            String imagenUtilizada = @"C:\Users\aleja\Documents\Universidad\Semestre8\Arquihard\ProyectoFinal\img\" + tam + ".bmp";


            switch (version)
                {
                    case 1:

                        AlgoritmoVersion_1(imagenUtilizada, tam);
                        break;

                    case 2:

                        AlgoritmoVersion_2(imagenUtilizada, tam);
                        break;

                    case 3:
                       
                        AlgoritmoVersion_3(imagenUtilizada, tam);
                        break;

                    case 4:

                        AlgoritmoVersion_4(imagenUtilizada, tam);
                        break;

                    case 5:

                        AlgoritmoVersion_5(imagenUtilizada, tam);
                        break;

                }


        }

    }
}
