{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Two_state_class.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "language_info": {
      "mimetype": "text/x-python",
      "nbconvert_exporter": "python",
      "name": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.6",
      "file_extension": ".py",
      "codemirror_mode": {
        "version": 3,
        "name": "ipython"
      }
    },
    "kernelspec": {
      "name": "python36",
      "display_name": "Python 3.6",
      "language": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/grkidwell/buckwaveforms/blob/master/two_state_class.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "id": "_xjdsGL1U2kX",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "class Two_state:\n",
        "    \n",
        "    def __init__(self,t1,t2):\n",
        "        self.t1 = t1\n",
        "        self.t2 = t2\n",
        "        self.Ts = t1+t2\n",
        "    \n",
        "# unit step function (in mathcad, was in kronicker delta section)\n",
        "    def step(self,t):\n",
        "        if t<0:\n",
        "            kd=0\n",
        "        elif t==0:\n",
        "            kd=0.5\n",
        "        else:\n",
        "            kd=1\n",
        "        return kd\n",
        "            \n",
        "# unit pulse functions have 'time' integer input and output a 1, 0 or 0.5\n",
        "    def t1_unit_pulse(self,t):\n",
        "        return self.step(self.t1-t)\n",
        "    \n",
        "    def t2_unit_pulse(self,t):\n",
        "        return (1-self.t1_unit_pulse(t)\n",
        "    \n",
        "    def repeating(self,t):\n",
        "        period=self.Ts\n",
        "        return t-(t//period)*period\n",
        "\n",
        "# pulse train functions have 'time' max input and output an array of 1's, 0's and 0.5's\n",
        "    def t1_pulse_train(self,tmax):\n",
        "        pulsetrain=[]\n",
        "        for t_idx in range(tmax):\n",
        "            pulsetrain.append(self.t1_unit_pulse(self.repeating(t_idx)))\n",
        "        return pulsetrain\n",
        "    \n",
        "    def t2_pulse_train(self,tmax):\n",
        "        pulsetrain=[]\n",
        "        for t_idx in range(tmax):\n",
        "            pulsetrain.append(self.t2_unit_pulse(self.repeating(t_idx)))\n",
        "        return pulsetrain\n",
        "    "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "id": "a04r-FjbU2kh",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}