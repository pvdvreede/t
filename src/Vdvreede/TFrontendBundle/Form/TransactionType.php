<?php

namespace Vdvreede\TFrontendBundle\Form;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilder;
use Vdvreede\TFrontendBundle\Entity;

class TransactionType extends AbstractType
{
    public function buildForm(FormBuilder $builder, array $options)
    {
        $builder->add('description', 'textarea');
        $builder->add('memo', 'textarea');
        $builder->add('date', 'date');
        $builder->add('reportable');
        $builder->add('amount', 'money', array(
            'currency' => 'USD'
        ));
        $builder->add('account', 'entity', array(
            'class' => 'Vdvreede\\TFrontendBundle\\Entity\\Account',
            'query_builder' => function($er) {
                return $er->createQueryBuilder('a')
                        ->where('a.userId = :userId')
                        ->setParameter('userId', 1);
            }
        ));
        $builder->add('category', 'entity', array(
            'class' => 'Vdvreede\\TFrontendBundle\\Entity\\Category',
            'query_builder' => function($er) {
                return $er->createQueryBuilder('c')
                        ->where('c.userId = :userId')
                        ->setParameter('userId', 1);
            }
        ));
    }
}