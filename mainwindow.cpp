#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>

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
    cout << "Button 2 clicked" << endl;
}

void MainWindow::on_txtName_textChanged(const QString &arg1)
{
    cout << "changed " << arg1 << endl;
}
