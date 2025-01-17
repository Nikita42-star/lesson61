# Домашнее задание по теме "Методы Юнит-тестирования"
# импорт библиотек и файлов
import unittest
import runner_and_tournament as rt


# класс TournamentTest, наследованный от TestCase
class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True
    # метод создания атрибута класса all_results
    # словарь в который будут сохраняться результаты всех тестов.
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # метод создания 3 объектов для тестов
    def setUp(self):
        self.run1 = rt.Runner('Усэйн', 10)
        self.run2 = rt.Runner('Андрей', 9)
        self.run3 = rt.Runner('Ник', 3)
        self.run4 = rt.Runner('Алекс', 5)

    # метод, где выводятся all_results (результаты теста) по очереди в столбец
    @classmethod
    def tearDownClass(cls):
        # объявление словаря
        result = {}
        # цикл перебора тестов
        for testkey, testval in cls.all_results.items():
            # вывод на консоль типа теста
            print(f'TEST: {testkey}')
            # цикл создания словаря участников теста
            for key, val in testval.items():
                # ввод данных результатов теста
                result[key] = str(val.name)
            # вывод на консоль участников теста по порядку
            print(result)

    # метод 1-го теста между участником 1 и 3 (название метода должно начинаться с test...)
    def testrun_1(self):
        # обращение к функции Tournament в файле runner_and_tournament
        run_1 = rt.Tournament(90, self.run1, self.run3)
        # получение результатов теста run1
        finish = run_1.start()
        # метод из класса TestCase в модуле unittest, который проверяет, истинность выражения
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        # присвоение self.all_results результатов теста между участниками
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    # метод 2-го теста между участником 2 и 3 (название метода должно начинаться с test...)
    def testrun_2(self):
        run_1 = rt.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    # метод 3-го теста между 3-мя участниками (название метода должно начинаться с test...)
    def testrun_3(self):
        run_1 = rt.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish


if __name__ == "__main__":
    unittest.main()