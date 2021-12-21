from behave import *
from pages.google_page import GooglePage

googlePage = GooglePage()

@given('que acesso a página do Google')
def step_impl(context):
    googlePage.acess_page('https://www.google.com.br/')

@given('que preencho o campo de pesquisa com calculadora')
def step_impl(context):
    googlePage.send_keys_input_pesquisa()

@when('clico no botão de pesquisa')
def step_impl(context):
    googlePage.click_button_pesquisa()

@when('clico no botão de numero 2')
def step_impl(context):
    googlePage.click_button_numero2()

@when('clico no botão de multiplicar')
def step_impl(context):
    googlePage.click_button_multiplicar()

@when('clico no botão de numero 1')
def step_impl(context):
    googlePage.click_button_numero1()
    
@when('clico no botão de numero 0')
def step_impl(context):
    googlePage.click_button_numero0()    

@when('clico no botão de igual')
def step_impl(context):
    googlePage.click_button_igual()
    
@when('acesso a página do Google')
def step_impl(context):
    googlePage.acess_page('https://www.google.com.br/')
    
@given('que preencho o campo de pesquisa com do a barrel roll')
def step_impl(context):
    googlePage.barrel_roll_input_pesquisa()
    
@when('volto a clicar no botão de pesquisa')
def step_impl(context):
    googlePage.click_button_pesquisa()
    
@when('volto a acessar a página do Google')
def step_impl(context):
    googlePage.acess_page('https://www.google.com.br/')

@when('volto a preencher o campo de pesquisa com google gravity')
def step_impl(context):
    googlePage.google_gravity_input_pesquisa()
    
@then('clico no botão estou com sorte')
def step_impl(context):
    googlePage.click_button_estou_com_sorte()