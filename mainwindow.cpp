#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>
#include <thread>

using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
  cout << "Button 1 clicked" << endl;
}

void MainWindow::on_pushButton_2_clicked()
{
  cout << "Bu tton 2 clicked" << endl;
}

void MainWindow::on_txtName_textChanged(const QString &arg1)
{
  cout << "changed " << arg1.toStdString() << endl;
}

void MainWindow::on_pushButton_clicked(bool checked)
{
    cout << "Clicked bool " << checked << endl;
 //   ui->
}

void MainWindow::on_verticalSlider_sliderMoved(int position)
{
    cout << "Slider moved " << position << endl;

    auto x = std::this_thread::get_id();

    //ui->pushButton->

    ui->progressbar->setValue(position);

    cout << x << endl;
}

void MainWindow::on_progressbar_valueChanged(int value)
{
    cout << "Progress bar changes" << endl;
}
